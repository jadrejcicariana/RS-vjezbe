from aiohttp import web

async def podijeli(request):
    data = await request.json()
    zbroj = data.get("zbroj")
    umnozak = data.get("umnozak")

    if zbroj == 0:
        return web.json_response(
            {"error": "dijeljenje s nulom nije dozvoljeno"},
            status=400
        )
    kolicnik = int(umnozak)/int(zbroj)
    return web.json_response(
        {"kolicnik": kolicnik},
        status=200
    )

app = web.Application()

app.router.add_post('/kolicnik', podijeli)

if __name__ == "__main__":
    web.run_app(app, port=8085)