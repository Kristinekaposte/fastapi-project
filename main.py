from fastapi.exceptions import HTTPException

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from exceptions import StoryException
from router import blog_get, blog_post
from db import models
from db.database import engine
from router import article, product, user

# run server with: uvicorn main:app --reload
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name}
    )


@app.exception_handler(HTTPException)
def custom_handler(request: Request, exc: StoryException):
    return PlainTextResponse(str(exc), status_code=400)


# Create the database tables
models.Base.metadata.create_all(engine)
