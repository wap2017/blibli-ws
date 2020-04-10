#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import user_pb2
import struct


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
            user = user_pb2.User()
            user.name = "张三"
            data = user.SerializeToString()

            l = len(data)
            format = ">I%us" % l
            print("format=", format)
            buf = struct.pack(format, l, data)

            await websocket.send(buf)
            print(f"> {user.name}")

            ret = await websocket.recv()
            print(f"< {ret}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(hello())
