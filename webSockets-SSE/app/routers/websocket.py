from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from services.connection_manager import ConnectionManager

manager = ConnectionManager()

app = FastAPI()
clients=[]

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)
    print("Client connected")

    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(message)

    except WebSocketDisconnect:
        # clients.disconnect(websocket)
        manager.disconnect(websocket)
        print("Client disconnected")

