#super zahtjevna operacija provjere parnosti broja

import asyncio
from random import randint

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        poruka = f"broj {broj} je paran"
    else:
        poruka = f"broj {broj} je neparan"
    return poruka
    
async def main():
    brojevi = [randint(0, 100) for x in range(0, 10)]
    zadaci = [asyncio.create_task(provjeri_parnost(i)) for i in brojevi]
    results = await asyncio.gather(*zadaci)
    print(results)

asyncio.run(main())
