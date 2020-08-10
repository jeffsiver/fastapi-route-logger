import asyncio
import logging
from unittest.mock import MagicMock, AsyncMock

import pytest
from fastapi import Request, Response, FastAPI, HTTPException

from fastapi_route_logger_middleware import RouteLoggerMiddleware


class TestRouteLogger:
    def test_exception_handler(self, mocker):
        response = MagicMock(spec=Response)
        http_exception_handler = mocker.patch(
            "fastapi_route_logger_middleware.http_exception_handler",
            return_value=response,
        )
        request = MagicMock(spec=Request, url=MagicMock(path="/ohno"), method="POST")
        logger = MagicMock(spec=logging.Logger)
        route_logger = RouteLoggerMiddleware(MagicMock(spec=FastAPI), logger=logger)
        exception = HTTPException(status_code=12, detail="something happened")

        result = asyncio.run(route_logger.exception_handler(request, exception))

        assert result == response
        http_exception_handler.assert_called_once_with(request, exception)
        logger.exception.assert_called_once_with(
            "Exception occurred processing request POST /ohno"
        )

    def test_when_skipping_route(self):
        request = MagicMock(spec=Request, url=MagicMock(path="/skip/me"))
        app = MagicMock(spec=FastAPI)
        logger = MagicMock(spec=logging.Logger)
        route_logger = RouteLoggerMiddleware(app, logger=logger, skip_routes=["/skip"])
        response = MagicMock(spec=Response)
        call_next = AsyncMock(return_value=response)
        result = asyncio.run(route_logger.dispatch(request, call_next))
        assert result == response
        call_next.assert_called_once_with(request)

    def test_when_logging_request(self, mocker):
        mocker.patch(
            "fastapi_route_logger_middleware.time.perf_counter", side_effect=[1.2, 1.4]
        )
        request = MagicMock(
            spec=Request, url=MagicMock(path="/somewhere",), method="GET"
        )
        app = MagicMock(spec=FastAPI)
        logger = MagicMock(spec=logging.Logger)
        route_logger = RouteLoggerMiddleware(app, logger=logger)
        response = MagicMock(spec=Response, status_code=200)
        call_next = AsyncMock(return_value=response)

        result = asyncio.run(route_logger.dispatch(request, call_next))

        assert result == response
        call_next.assert_called_once_with(request)
        logger.info.assert_called_once_with(
            "Request successful, GET /somewhere, status code=200, took=0.2000s"
        )

    def test_when_logging_request_with_standard_exception(self, mocker):
        mocker.patch(
            "fastapi_route_logger_middleware.time.perf_counter", side_effect=[1.2, 1.4]
        )
        request = MagicMock(
            spec=Request, url=MagicMock(path="/somewhere",), method="GET"
        )
        app = MagicMock(spec=FastAPI)
        logger = MagicMock(spec=logging.Logger)
        route_logger = RouteLoggerMiddleware(app, logger=logger)
        call_next = AsyncMock(side_effect=Exception("nothing good will come of this"))

        with pytest.raises(Exception):
            asyncio.run(route_logger.dispatch(request, call_next))

        call_next.assert_called_once_with(request)
        logger.exception.assert_called_once_with(
            f"Request failed with exception /somewhere, method=GET"
        )
