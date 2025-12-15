from aiohttp import web

async def zbroji(request):
    lista = await request.json()

    if not isinstance(lista, list):
        return web.json_response({"error": "nije proslijedena lista"}, status=400)
    
    return web.json_response(
        {"zbroj": sum(lista)},
        status=200
    )

app = web.Application()

app.router.add_post('/zbroj', zbroji)

if __name__ == "__main__":
    web.run_app(app, port=8083)