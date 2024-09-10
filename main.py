from fastapi import FastAPI
from database import Base, engine
from routers import auth

app = FastAPI(
    title='Todo App',
    description='Track todos for every user',
    version='1.0.0'
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get('/')
async def index():
    return {'request': 'Hello World!'}
