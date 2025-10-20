from fastapi import FastAPI, Depends, status, Response, HTTPException
from blog.schemas import Blog, ShowBlog, User, ShowUser
from blog import models
from blog.database import engine, sessionLocal, get_db
from sqlalchemy.orm import Session
from typing import List
from blog.hasing import Hash
from blog.routers import blog

app = FastAPI()

# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)


