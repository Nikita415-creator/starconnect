# relay_ws.py (исправленный)
import asyncio
import websockets

clients = set()

async def handler(ws, path):
    clients.add(ws)
    try:
        async for message in ws:
            for c in clients:
                if c != ws:
                    await c.send(message)
    finally:
        clients.remove(ws)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 443):
        print("Relay запущен на порту 443…")
        await asyncio.Future()  # чтобы сервер не завершался

asyncio.run(main())