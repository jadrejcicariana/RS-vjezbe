#get proizvodi

from aiohttp import web


async def get_proizvodi(request):
    data = [{"naziv": "proizvod1", "cijena": 25, "kolicina": 3}]
    return web.json_response(data)


app = web.Application()

app.router.add_routes([
    web.get('/proizvodi', get_proizvodi)
])

web.run_app(app, port=8081)