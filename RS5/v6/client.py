import aiohttp
import asyncio
import time

async def get_poz(url, port):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'http://{url}:{port}/pozdrav')
        return await response.json()



async def main():
    print("Pokrecem main korutinu")

    #sekvencijalno
    #response1 = await get_poz("localhost", 8081)
    #print(f"odgovor od ms1: {response1}")

    #response2 = await get_poz("localhost", 8082)
    #print(f"odgovor od ms2: {response2}")

    #konkurentno
    t1 = time.time()
    results = await asyncio.gather(
        get_poz("localhost", 8081),
        get_poz("localhost", 8082)
    )
    t2 = time.time()
    print(f"Vrijeme: {t2 - t1:.2f} sekundi")
    print(results)



asyncio.run(main())