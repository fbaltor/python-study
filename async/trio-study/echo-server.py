import trio
from itertools import count

PORT = 1234

CONN_COUNTER = count()

async def echo_server(server_stream):
    identifier = next(CONN_COUNTER)
    print(f"echo_server {identifier}: started")
    try:
        async for data in server_stream:
            print(f"echo_server {identifier}: received data {data!r}")
            await server_stream.send_all(data)
        print(f"echo_server {identifier}: connection closed")
    except Exception as exc:
        print(f"echo_server {identifier}: crashed: {exc!r}")

async def main():
    await trio.serve_tcp(echo_server, PORT)

trio.run(main)
