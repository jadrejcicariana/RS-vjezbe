#dvije korutine dohvacanje podataka s weba, konkurentno

import asyncio
import time

async def dohvati_korisnike():
    korisnici = [
        {"id": "1", "ime": "ivan", "prezime": "ivic"},
        {"id": "2", "ime": "luka", "prezime": "lukic"},
        {"id": "3", "ime": "marko", "prezime": "markovic"}
    ]
    await asyncio.sleep(3)
    return korisnici

async def dohvati_proizvode():
    proizvodi = [
        {"id": "1", "naziv": "mis", "cijena": 20},
        {"id": "2", "naziv": "tipkovnica", "cijena": 70},
        {"id": "3", "naziv": "monitor", "cijena": 200}
    ]
    await asyncio.sleep(5)
    return proizvodi

async def main():
    tasks = [asyncio.create_task(dohvati_korisnike()), asyncio.create_task(dohvati_proizvode())]
    t1 = time.perf_counter()
    results = await asyncio.gather(*tasks)
    t2 = time.perf_counter()
    print(results)
    print(f"Vrijeme izvodenja {t2 - t1:.2f} sekunde")
    
    
asyncio.run(main())
