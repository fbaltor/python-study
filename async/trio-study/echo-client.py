import sys
import trio

PORT = 1234

async def sender(client_stream):
    print("sender: started!")
    while True:
        data = b"some random message"
        print(f"sender: sending {data!r}!")
        await client_stream.send_all(data)
        await trio.sleep(1)

async def receiver(client_stream):
    print("receiver: started!")
    async for data in client_stream:
        print(f"receiver: got data {data!r}")
    print("receiver: connection closed")
    sys.exit()

async def parent():
    print(f"parent: connecting to localhost:{PORT}")
    client_stream = await trio.open_tcp_stream("localhost", PORT)
    async with client_stream:
        async with trio.open_nursery() as nursery:
            print("parent: spawning sender...")
            nursery.start_soon(sender, client_stream)

            print("parent: spawning receiver...")
            nursery.start_soon(receiver, client_stream)

trio.run(parent)
