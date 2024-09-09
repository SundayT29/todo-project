from fastapi import FastAPI
from database import Base, engine
import models

app = FastAPI(
    title='Todo App',
    description='Track todos for every user',
    version='1.0.0'
)

Base.metadata.create_all(bind=engine)

@app.get('/')
async def index():
    return {'request': 'Hello World!'}

