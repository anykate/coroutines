import asyncio
import time


async def run_task(task):
    result = await task
    print(f'Received result: {result}')


async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay)
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id}


async def main():
    print("Start of main coroutine")
    tasks = []

    start = time.time()

    [tasks.append(asyncio.create_task(fetch_data(10, i))) for i in range(4)]
    [await run_task(tasks[i]) for i in range(len(tasks))]

    end = time.time()
    print(f"Total time: {end - start} seconds!")


if __name__ == "__main__":
    asyncio.run(main())
