#!/usr/bin/env python

# WS client example

import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            name = input("What's your name? ")

            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(hello())
