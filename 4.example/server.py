#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import struct
import user_pb2


async def hello(websocket, path):
        buf = await websocket.recv()

        l = (buf[0] << 24) + (buf[1] << 16) + (buf[2] << 8) + buf[3]
        print('l=', l)
        format = ">%us" % l
        data = struct.unpack(format, buf[4:])
        print(data)
        user = user_pb2.User()
        user.ParseFromString(buf[4:])
        print("服务器收到名字, name=", user.name)

        greeting = f"I received!"
        await websocket.send(greeting)
        print(f"> {greeting}")


if __name__ == "__main__":
    start_server = websockets.serve(hello, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
