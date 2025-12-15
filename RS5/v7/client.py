import asyncio
from aiohttp import ClientSession

lista = [2, 3, 4]

async def main():
    async with ClientSession() as session:
        zbroj = session.post(
            "http://localhost:8083/zbroj",
            json = lista
        )

        umnozak = session.post(
            "http://localhost:8084/umnozak",
            json = lista
        )

        rez_zbroj, rez_umnozak = await asyncio.gather(zbroj, umnozak)

        zbroj_json = await rez_zbroj.json()
        print(zbroj_json)
        umnozak_json = await rez_umnozak.json()
        print(umnozak_json)

        rez_kolicnik = await session.post(
            "http://localhost:8085/kolicnik",
            json = {
                "zbroj": zbroj_json["zbroj"],
                "umnozak": umnozak_json["umnozak"]
            }
        )

        print(await rez_kolicnik.json())

asyncio.run(main())