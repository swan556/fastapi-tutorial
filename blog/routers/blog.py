from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog.schemas import *
from typing import List
from blog.database import get_db
from blog import models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get('/', response_model=List[ShowBlog])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id,response:Response, db:Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f"blog with id {id} is not available"}
    return blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.update(dict(request))
    db.commit()
    return request

