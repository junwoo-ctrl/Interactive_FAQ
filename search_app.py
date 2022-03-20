import asyncio

import uvicorn
import uvloop
from fastapi import FastAPI

from rest.health_check import router as health_check_router
from rest.async_vector_search import router as async_vector_search


def create_app():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = FastAPI(
        docs_url="/search-knn/docs",
        openapi_url="/search-knn/openapi.json",
    )
    
    return app


def include_router(application: FastAPI):
    application.include_router(health_check_router)
    application.include_router(async_vector_search)


app = create_app()
include_router(app)


if __name__ == "__main__":
    uvicorn.run("search_app:app", host="0.0.0.0", port=9999, reload=False)
