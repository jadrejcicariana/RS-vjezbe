from aiohttp import web

async def pomnozi(request):
    lista = await request.json()

    if not isinstance(lista, list):
        return web.json_response({"error": "nije proslijedena lista"}, status=400)
    
    sum = 1
    for x in lista:
        sum *= x
    
    return web.json_response(
        {"umnozak": sum},
        status=200
    )

app = web.Application()

app.router.add_post('/umnozak', pomnozi)

if __name__ == "__main__":
    web.run_app(app, port=8084)