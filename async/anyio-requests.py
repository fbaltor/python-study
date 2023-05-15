import anyio
import httpx
import time

URL = 'https://example.org/'

async def request(client, i):
    response = await client.get(URL)

async def main():

    limits = httpx.Limits(max_keepalive_connections=500, max_connections=500)
    client  = httpx.AsyncClient(limits=limits, timeout=None)

    async with anyio.create_task_group() as tg:
        for i in range(100):
            tg.start_soon(request, client, i)

    await client.aclose()

    print('All requests finished!')

start_time = time.time()
anyio.run(main)
print(f'--- {time.time() - start_time} seconds ---')
