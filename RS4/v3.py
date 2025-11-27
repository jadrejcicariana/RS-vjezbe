#mix_dog_cat_facts

import asyncio
import aiohttp

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    fact = await response.json()
    return fact["data"][0]["attributes"]["body"]

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact = await response.json()
    return fact["fact"]

async def mix_facts(dog_facts, cat_facts):
    facts = [max(dog_fact, cat_fact, key=len) for dog_fact, cat_fact in zip(dog_facts, cat_facts)]
    return facts

async def main():

    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [get_dog_fact(session) for i in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for i in range(5)]
        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]
    facts = await mix_facts(dog_facts, cat_facts)

    for fact in facts:
        print("-", fact)


asyncio.run(main())