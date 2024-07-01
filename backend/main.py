from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

async def fake_data_streamer():
    for i in range(10):
        yield f"data: {i}\n\n"
        await asyncio.sleep(1)

@app.get("/stream")
async def stream():
    return StreamingResponse(fake_data_streamer(), media_type="text/event-stream")


