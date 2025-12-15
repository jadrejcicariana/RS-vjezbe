#proizvodi i ruta za narudzbe

from aiohttp import web, ClientSession
import asyncio


proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Miš", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def get_proizvodi(request):
    id = request.match_info.get("id")

    if id is None:
        return web.json_response(proizvodi, status=200)
    
    for proizvod in proizvodi:
        if proizvod["id"] == int(id):
            return web.json_response(proizvod, status=200)
    
    return web.json_response({"error": "proizvod ne postoji"}, status=404)
    
async def post_narudzbe(request):
    narudzba = await request.json()
    proizvod_id = narudzba.get("proizvod_id")
        
    for proizvod in proizvodi:
        if proizvod["id"] == proizvod_id:
            narudzbe.append(narudzba)
            return web.json_response(narudzbe, status=201)
        
    return web.json_response({"error": "proizvod ne postoji"}, status=404)    
    

async def start_server():
    app = web.Application()
    app.router.add_get("/proizvodi", get_proizvodi)
    app.router.add_get("/proizvodi/{id}", get_proizvodi)
    app.router.add_post("/narudzbe", post_narudzbe)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()
    print("Posluzitelj slusa")

async def main():
    asyncio.create_task(start_server())
    
    async with ClientSession() as session:
        print("Klijentska sesija otvorena")

        #svi proizvodi
        rez1 = await session.get("http://localhost:8081/proizvodi")
        rez1 = await rez1.json()
        print(rez1)

        #proizvod koji postoji
        rez2 = await session.get("http://localhost:8081/proizvodi/1")
        rez2 = await rez2.json()
        print(rez2)

        #proizvod koji ne postoji
        rez3 = await session.get("http://localhost:8081/proizvodi/6")
        rez3 = await rez3.json()
        print(rez3)

        #dodavanje narudzbe
        rez4 = await session.post(
            "http://localhost:8081/narudzbe",
            json = {
                "proizvod_id": 1,
                "kolicina": 2
            })
        print(await rez4.json())

        #dodavanje narudzbe, ali proizvod ne postoji
        rez5 = await session.post(
            "http://localhost:8081/narudzbe",
            json = {
                "proizvod_id": 7,
                "kolicina": 2
            })
        print(await rez5.json())
        
    await asyncio.Event().wait()    

asyncio.run(main())