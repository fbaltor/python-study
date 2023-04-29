import time
import trio

async def broken_double_sleep(x):
    print("*yawn* Going to sleep")
    start_time = time.perf_counter()

    await trio.sleep(2 * x)

    sleep_time = time.perf_counter() - start_time
    print(f"Woke up after {sleep_time:.2f} seconds, feeling well rested!")

trio.run(broken_double_sleep, 1)
