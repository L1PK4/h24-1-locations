from contextlib import asynccontextmanager
from fastapi import FastAPI
from service.app.settings import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan, docs_url='/docs', redoc_url='/redoc')

    return app