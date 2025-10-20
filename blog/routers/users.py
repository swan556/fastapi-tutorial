from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog.schemas import *
from typing import List
from blog.database import get_db
from blog import models
from sqlalchemy.orm import Session
from blog.hashing import Hash

router = APIRouter(
    tags=["user"],
    prefix="/user"
    )

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def show_user(id, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} is not available"
        )
    return user