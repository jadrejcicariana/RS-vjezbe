import asyncio
from aiohttp import ClientSession

async def get_facts(session, amount):
    
    async with session.get(f"http://localhost:8086/cat/{amount}") as response:
        
        data = await response.json()
        return data.get("facts", [])

async def filter_facts(session, facts):
    
    async with session.post("http://localhost:8087/facts", json=facts) as response:
        
        data = await response.json()
        return data.get("facts", [])

async def main():
    amount = 10

    async with ClientSession() as session:
        
        facts = await get_facts(session, amount)
        print("facts: ")
        for f in facts:
            print("-", f)

        filtered_facts = await filter_facts(session, facts)
        print("filtrirano: ")
        for f in filtered_facts:
            print("-", f)

asyncio.run(main())
