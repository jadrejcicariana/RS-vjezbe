#post proizvodi

from aiohttp import web

data = [{"naziv": "proizvod1", "cijena": 25, "kolicina": 3}]

async def get_proizvodi(request):
    
    return web.json_response(data)

async def add_proizvodi(request):
    proizvod = await request.json()
    data.append(proizvod)
    print(f"primljeni podaci: {proizvod}")
    return web.json_response(data)


app = web.Application()

app.router.add_routes([
    web.get('/proizvodi', get_proizvodi),
    web.post('/proizvodi', add_proizvodi)
])

web.run_app(app, port=8081)