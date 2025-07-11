import os

# add the parent directory to system path so we can run api_server.py from the src directory
import sys

sys.path.append(os.path.dirname(os.path.dirname("../")))

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from utils import logger, settings

from api.api_route import router, TagEnum
from api.routers.parking import router as parking_router

app = FastAPI(title="Parking Management System API", version="1.0.0")

# ROUTERS
routers = [router, parking_router]
for router in routers:
    app.include_router(router)


@app.get("/", tags=[TagEnum.general])
async def root():
    logger.debug("Server is up and running!")

    logger.debug(f"Settings: {settings}")

    return JSONResponse(content="FastAPI server is up and running!")
