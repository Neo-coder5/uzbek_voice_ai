from fastapi import FastAPI, WebSocket
import whisper

app = FastAPI()

model = whisper.load_model("base")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    audio_parts = []

    while True:
        audio = await websocket.receive_bytes()

        print("Audio bo'lagi keldi:", len(audio), "bytes")

        audio_parts.append(audio)

        print("Jami bo'laklar:", len(audio_parts))

        await websocket.send_text(
            f"Audio qabul qilindi: {len(audio_parts)}-bo'lak"
        )
