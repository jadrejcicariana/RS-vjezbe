#Objasnite korak po korak kako se ponaša event loop

import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())

#prvo se kreiraju taskovi redom timer 1, timer 2, timer 3
#gather ih runna istim redom
#krece sa izvodenjem timer 1, ispisuje 3 sekunde preostalo
#kad on ode u sleep 1 sekundu, krece sa izvodenjem timer 2
#timer 2 ispisuje 5 sekundi preostalo, i ide u sleep
#krece s izvodenjem timer 3, ispisuje 7 sekundi preostalo, ide u sleep
#opet se nastavlja timer 1, sad mu je 2 sekunde preostalo... itd
#vrte se u loop, svaki put kad neki od njih ode u sleep prebacuje se na iduci,
#dok se ne pozavrsavaju

