from anyio import sleep, create_task_group, run


async def sometask(num):
    print('Task', num, 'running')
    await sleep(1)
    print('Task', num, 'finished')


async def main():
    async with create_task_group() as tg:
        for num in range(5):
            tg.start_soon(sometask, num)

    print('All tasks finished!')

run(main)

