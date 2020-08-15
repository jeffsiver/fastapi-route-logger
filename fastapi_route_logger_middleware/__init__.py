import logging
import time
import typing
from typing import Callable

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class RouteLoggerMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: FastAPI,
        *,
        logger: typing.Optional[logging.Logger] = None,
        skip_routes: typing.List[str] = None,
    ):
        self._logger = logger if logger else logging.getLogger(__name__)
        self._skip_routes = skip_routes if skip_routes else []
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if self._should_route_be_skipped(request):
            return await call_next(request)

        return await self._execute_request_with_logging(request, call_next)

    def _should_route_be_skipped(self, request: Request) -> bool:
        return any(
            [path for path in self._skip_routes if request.url.path.startswith(path)]
        )

    async def _execute_request_with_logging(
        self, request: Request, call_next: Callable
    ) -> Response:
        start_time = time.perf_counter()

        response = await self._execute_request(call_next, request)

        finish_time = time.perf_counter()
        self._logger.info(
            self._generate_success_log(request, response, finish_time - start_time)
        )

        return response

    def _generate_success_log(
        self, request: Request, response: Response, execution_time: float
    ):
        overall_status = "successful" if response.status_code < 500 else "failed"
        return f"Request {overall_status}, {request.method} {request.url.path}, status code={response.status_code}, took={execution_time:0.4f}s"

    async def _execute_request(self, call_next: Callable, request: Request) -> Response:
        try:
            response = await call_next(request)
        except Exception:
            self._logger.exception(
                f"Request failed with exception {request.url.path}, method={request.method}"
            )
            raise
        return response
