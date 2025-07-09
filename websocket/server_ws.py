import asyncio
import websockets

async def handler(ws):
    print("Client connected")
    async for message in ws:
        print("Received:", message)

async def main():
    async with websockets.serve(handler, '127.0.0.1', 8081):
        print("WebSocket server listening on ws://127.0.0.1:8081")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
