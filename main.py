from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        audio = await websocket.receive_bytes()
        print("Audio received:", len(audio), "bytes")
        await websocket.send_text("Audio received")


