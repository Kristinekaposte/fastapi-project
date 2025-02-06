from fastapi import FastAPI
from router import blog_get
from router import blog_post

# run server with: uvicorn main:app --reload
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get("/")
def index():
    return {"message": "Hello World"}





