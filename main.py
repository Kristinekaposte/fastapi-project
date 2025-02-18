from fastapi import FastAPI
from router import blog_get
from router import blog_post
from db import models
from db.database import engine
from router import user
from router import article

# run server with: uvicorn main:app --reload
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)

@app.get("/")
def index():
    return {"message": "Hello World"}

# Create the database tables
models.Base.metadata.create_all(engine)



