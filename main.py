from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name':'Swan'}}

@app.get('/about')
def about():
    return 'lalala'