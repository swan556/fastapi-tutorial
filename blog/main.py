from fastapi import FastAPI
from blog.schemas import Blog
app = FastAPI()

@app.post('/blog')
def create(request: Blog):
    return request