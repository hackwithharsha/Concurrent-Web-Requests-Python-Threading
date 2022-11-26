from fastapi import FastAPI, Query
import asyncio
import random
import uvicorn

app = FastAPI()

STATUSES = ['PENDING', 'FAILED', 'STARTED', 'SUCCESS']

@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/status")
async def get_status(
    task_id: int =  Query(...)
):
    await asyncio.sleep(5)
    return {
        'task_id': task_id,
        'status': random.choice(STATUSES)
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

