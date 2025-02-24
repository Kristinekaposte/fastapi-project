from fastapi.exceptions import HTTPException

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from exceptions import StoryException
from router import blog_get, blog_post, article, product, user, file
from db import models
from db.database import engine
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# run server with: uvicorn main:app --reload
app = FastAPI()
app.include_router(authentication.router)
app.include_router(file.router)
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


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


# Create the database tables
models.Base.metadata.create_all(engine)

origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)

app.mount('/files', StaticFiles(directory="files"), name='files')