from fastapi import FastAPI

from routers.websocket import router as websocket_router
from routers.sse import router as sse_router

app = FastAPI(
    title="Week 3 Real-Time API"
)

app.include_router(websocket_router)
app.include_router(sse_router)


