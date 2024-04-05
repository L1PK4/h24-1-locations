from contextlib import asynccontextmanager
from fastapi import FastAPI
from service.app.settings import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    return app