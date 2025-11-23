import json
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

# Local modules
from collector import collect_live_data
from processor import process_data

app = FastAPI()

# Allow any origin for development (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# In‑memory set of connected websockets
connected_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            await asyncio.sleep(0.1)  # keep connection alive
    except WebSocketDisconnect:
        connected_clients.discard(websocket)

async def broadcast_updates(interval: int = 5):
    """Periodically collect raw data, process it, and push to all clients."""
    while True:
        raw = await collect_live_data()
        payload = process_data(raw)
        message = json.dumps(payload)
        # Broadcast to all connected clients
        for ws in list(connected_clients):
            try:
                await ws.send_text(message)
            except Exception:
                connected_clients.discard(ws)
        await asyncio.sleep(interval)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(broadcast_updates())

@app.get("/", response_class=HTMLResponse)
async def get_root():
    return "<html><body><h1>F1 Live Stats Backend</h1></body></html>"
