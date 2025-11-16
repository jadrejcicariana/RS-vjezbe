#enkripcija osjetljivih podataka

import asyncio

data = [
    {"prezime": "ivic", "br_kartice": "123456789", "cvv": "123"},
    {"prezime": "lukic", "br_kartice": "123456788", "cvv": "456"},
    {"prezime": "anic", "br_kartice": "123456777", "cvv": "789"},
]

async def secure_data(rjecnik):
    await asyncio.sleep(3)
    rjecnik["br_kartice"] = hash(rjecnik["br_kartice"])
    rjecnik["cvv"] = hash(rjecnik["cvv"])
    return rjecnik

async def main():
    zadaci = [asyncio.create_task(secure_data(i)) for i in data]
    results = await asyncio.gather(*zadaci)
    print(results)

asyncio.run(main())