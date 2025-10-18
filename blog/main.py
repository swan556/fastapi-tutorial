from fastapi import FastAPI, Depends
from blog.schemas import Blog
from blog import models
from .database import engine
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = Session
models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: Blog, db: Session = Depends(get_db)):
    return request