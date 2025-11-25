#filter cat facts

import aiohttp
import asyncio

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact = await response.json()
    return fact["fact"]

async def filter_cat_facts(results):
    return [fact for fact in results if "cat" in fact.lower() or "cats" in fact.lower()]

async def main():

    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session) for i in range(20)]
        results = await asyncio.gather(*tasks)

    facts = await filter_cat_facts(results)
    for fact in facts:
        print("-", fact)

asyncio.run(main())