#korutina koja ce simulirati dohvacanje podataka s weba

import asyncio

async def dohvati():
    lista = [x for x in range(1, 11)]
    await asyncio.sleep(3)
    print("podaci dohvaceni")
    print(lista)
    return lista

asyncio.run(dohvati())