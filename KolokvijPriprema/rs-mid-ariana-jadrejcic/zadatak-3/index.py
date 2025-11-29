import time
import asyncio
import requests
import aiohttp

#3.1
def zadatak(sekunde: int) -> str:
    time.sleep(sekunde)
    return f"zadatak zavrsen nakon {sekunde} sekundi"

def main():
    print(zadatak(3))
    print(zadatak(2))
    print(zadatak(1))
        
#t1 = time.perf_counter()
#main()
#t2 = time.perf_counter()
#print(f"vrijeme izvodenja: {(t2 - t1): .2f}")


#3.2
async def asinkroni_zadatak(sekunde: int) -> str:
    await asyncio.sleep(sekunde)
    return f"zadatak zavrsen nakon {sekunde} sekundi"

async def main():
    t1 = asyncio.create_task(asinkroni_zadatak(3))
    t2 = asyncio.create_task(asinkroni_zadatak(2))
    t3 = asyncio.create_task(asinkroni_zadatak(1))
    #await t1
    #await t2
    #await t3
    await asyncio.gather(t1, t2, t3)

#t1 = time.perf_counter()
#asyncio.run(main())
#t2 = time.perf_counter()
#print(f"vrijeme izvodenja: {(t2 - t1): .2f}")  

#event loop: svi schedulani taskovi se izvode konkurentno, 
#kako koji ode u sleep tako izvodenje prelazi na iduci

#3.3
def posalji_zahtjev(url: str) -> dict:
    rez = requests.get(url).json()
    return rez


def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    lista = []
    for i in range (1, 4):
        rez = posalji_zahtjev(url)
        lista.append(rez["title"])
    print(lista)


#t1 = time.perf_counter()
#main()
#t2 = time.perf_counter()
#print(f"vrijeme izvodenja: {(t2 - t1): .2f}")   

#3.4
async def posalji_zahtjev(url: str, session: aiohttp.ClientSession) -> dict:
    rez = await session.get(url)
    rez = await rez.json()
    return rez["title"]


async def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    async with aiohttp.ClientSession() as session:
        tasks = [posalji_zahtjev(url, session) for i in range(3)]
        results = await asyncio.gather(*tasks)
        print(results)


t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"vrijeme izvodenja: {(t2 - t1): .2f}")  

#asinkrono je brze, zato jer ne gubimo vrijeme cekajuci na svaki odgovor