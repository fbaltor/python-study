import httpx
import anyio
import time

async def request(client):
    response = await client.get('https://example.org/')

async def main():
    async with httpx.AsyncClient() as client:
        async with anyio.create_task_group() as tg:
            for num in range(1000):
                tg.start_soon(request, client)

start_time = time.time()
anyio.run(main, backend='trio')
print(f'--- {time.time() - start_time} seconds ---')

