#pretvorba sinkronog koda u asinkroni

import aiohttp
import asyncio

async def fetch_url(session, url: str) -> str:
    response = await session.get(url, timeout=5)
    return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    for x, y in zip(results, urls):
        print(f"fetched {len(x)} characters from {y}")
    
asyncio.run(main())