import logging.config
from time import sleep

from fastapi import FastAPI, HTTPException

from fastapi_route_logger_middleware import RouteLoggerMiddleware

app = FastAPI(title="Sample API for testing logging", version="1.0")

logging.config.fileConfig("./logging.conf")
app.add_middleware(RouteLoggerMiddleware)


@app.get("/success")
def success_endpoint():
    sleep(1)
    return "happy"


@app.get("/failed")
def failed_endpoint():
    raise HTTPException(status_code=500)
