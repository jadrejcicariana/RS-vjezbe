from aiohttp import web

async def filter(request):
    data = await request.json()
    
    filtrirano = [fact for fact in data if "cat" in fact.lower()]

    return web.json_response(
        {"facts": filtrirano},
        status=200
    )

app = web.Application()

app.router.add_post('/facts', filter)

if __name__ == "__main__":
    web.run_app(app, port=8087)