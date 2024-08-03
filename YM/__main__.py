from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import socketio

# Create a new Async SocketIO server
sio = socketio.AsyncServer(async_mode='asgi')
app = FastAPI()

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="YM/static"), name="static")

# Create a new ASGI application combining FastAPI and SocketIO
app_asgi = socketio.ASGIApp(sio, app)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = Path("YM/templates/index.html").read_text()
    return HTMLResponse(content=html_content)

# Define SocketIO events
@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

@sio.event
async def message(sid, data):
    print("Message from", sid, ":", data)
    await sio.emit('response', {'data': 'Hello from server'}, room=sid)
