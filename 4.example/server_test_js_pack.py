#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import struct
import user_pb2


async def hello(websocket, path):
        buf = await websocket.recv()
        print(buf)
        print(type(buf))
        format = ">HI"
        data = struct.unpack(format, buf)
        print(data)


if __name__ == "__main__":
    start_server = websockets.serve(hello, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
