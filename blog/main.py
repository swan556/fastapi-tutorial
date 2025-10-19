from fastapi import FastAPI, Depends, status, Response
from blog.schemas import Blog
from blog import models
from blog.database import engine, sessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
models.Base.metadata.create_all(engine)

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id,response:Response, db:Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f"blog with id {id} is not available"}
    return blog