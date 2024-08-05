import asyncio

async def fetch_data(delay, data):
    print(f"start fetching {data}...")
    await asyncio.sleep(delay)
    print(f"finished fetching {data}...")

    return data

async def main():
    task1 = asyncio.create_task(fetch_data(2, "data1"))
    task2 = asyncio.create_task(fetch_data(3, "data2"))
    task3 = asyncio.create_task(fetch_data(1, "data3"))

    results = await asyncio.gather(task1, task2, task3)
    print(f"results: { results}")

asyncio.run(main())