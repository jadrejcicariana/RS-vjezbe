#simulacija rs za vremenske podatke

import asyncio
import random

async def fetch_weather_data(location):
    try:
        await asyncio.wait_for(asyncio.sleep(random.uniform(1, 5)), timeout = 2)
        temp = random.randint(20, 25)
        print(f"temperatura na lokaciji {location}: {temp}")
        return temp
    except asyncio.TimeoutError:
        print(f"Timeout while fetching data from location {location}")
        return None

async def main():
    tasks = [asyncio.create_task(fetch_weather_data(location)) for location in range (1, 11)]
    results = await asyncio.gather(*tasks)
    print(f"temperature: {results}")
    results = [x for x in results if x is not None]
    try:
        avg = (sum(results))/len(results)
        print(f"prosjecna temperatura je: {avg: .2f}")
    except ZeroDivisionError:
        print("No data")
    

asyncio.run(main())