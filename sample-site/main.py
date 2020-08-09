import logging.config
from time import sleep

from fastapi import FastAPI, HTTPException

from route_logger import RouteLogger

app = FastAPI(title="Sample API for testing logging", version="1.0")

logging.config.fileConfig("./logging.conf")
app.add_middleware(RouteLogger)


@app.get("/success")
def success_endpoint():
    sleep(1)
    return "happy"


@app.get("/failed")
def failed_endpoint():
    raise HTTPException(status_code=500)
