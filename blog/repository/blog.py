from sqlalchemy.orm import Session
from blog import models

def get_all(db: Session):
    return db.query(models.Blog).all()