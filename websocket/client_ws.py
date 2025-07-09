import asyncio
import websockets

async def send_loop():
    uri = "ws://127.0.0.1:8081"
    async with websockets.connect(uri) as ws:
        while True:
            msg = "Hello"
            await ws.send(msg)
            print("Sent:", msg)
            await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(send_loop())
