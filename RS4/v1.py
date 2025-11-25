#fetch_users i izdvajanje podataka

import aiohttp
import asyncio
import time

async def fetch_users(session):
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    users = await response.json()
    return users

async def main():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for i in range(5)]
        results = await asyncio.gather(*tasks)

    users = [user for request in results for user in request]
    names = [x["name"] for x in users]
    emails = [x["email"] for x in users]
    usernames = [x["username"] for x in users]
    
    print(names, emails, usernames)
        
    end = time.perf_counter()
    
    print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")

asyncio.run(main())