import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from service.app.app import create_app

if __name__ == "__main__":
    app = create_app()
    asyncio.run(serve(app, Config()))
