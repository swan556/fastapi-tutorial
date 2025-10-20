from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, users

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(users.router)

