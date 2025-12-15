from aiohttp import web, ClientSession
import asyncio

api = "https://catfact.ninja/fact"
api2 = "https://catfact.ninja/facts"


async def get_facts(request):
    async with ClientSession() as session:
        async with session.get(api2) as response:
            data = await response.json()
            return web.json_response(data)


async def get_fact(session):
    async with session.get(api) as response:
        data = await response.json()
        return data.get("fact")


async def get_facts_amt(request):
    amount = int(request.match_info.get("amount", 1))

    async with ClientSession() as session:

        tasks = [get_fact(session) for i in range(amount)]
        facts = await asyncio.gather(*tasks)

    return web.json_response({"facts": facts})


app = web.Application()
app.router.add_get("/cat/{amount}", get_facts_amt)
app.router.add_get("/cats", get_facts)

if __name__ == "__main__":
    web.run_app(app, port=8086)
