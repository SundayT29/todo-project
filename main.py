from fastapi import FastAPI
import uvicorn  # This is the ASGI server to run FastAPI

app = FastAPI(
    title='Todo App',
    description='Track todos for every user',
    version='1.0.0'
)

@app.get('/')
async def index():
    return {'request': 'Hello World!'}
