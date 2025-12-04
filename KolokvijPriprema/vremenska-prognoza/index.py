from VremenskaPrognoza import VremenskaPrognoza

from datetime import datetime, timedelta
import asyncio
import random
import time


#neki_datum = datetime(1999, 7, 1)

#instanca = VremenskaPrognoza("Zagreb", 25, neki_datum)
#instanca.ispis()


async def simuliraj_temperaturu(broj_dana: int, isCool: bool):
    lista = []
    for i in range(1, broj_dana):
        if isCool:
            temperatura_zraka = random.randint(0, 20) 
        else:
            temperatura_zraka = random.randint(20, 40)
        lista.append((i, temperatura_zraka))
        await asyncio.sleep(0.1)
    return lista

#async def main():
    #task1 = await asyncio.create_task(simuliraj_temperaturu(10, True))
    #task2 = await asyncio.create_task(simuliraj_temperaturu(10, False)) 1.96s sekvencijalno
    
    #task1 = asyncio.create_task(simuliraj_temperaturu(10, True))
    #task2 = asyncio.create_task(simuliraj_temperaturu(10, False))
    #rez = await asyncio.gather(task1, task2) #0.97s konkurentno
    #print(rez)    


#t1 = time.perf_counter()
#asyncio.run(main())
#t2 = time.perf_counter()
#print(f"vrijeme izvodenja: {(t2 - t1): .2f}")  

#duplo je brze konkurentno, zato jer sekvencijalno prvo izvrsi prvi task pa tek onda drugi
#a konkurentno prelazi na drugi task svaki put kad prvi ide u sleep

#zadatak 3
async def simuliraj_sljedecih_mjesec_dana(lista, instanca):
    for dan in lista:
        datum = instanca.datum + timedelta(days=1)
        instanca.dnevna_promjena((dan[1]), datum)
        instanca.ispis()


async def main():
    hladni_dani = await asyncio.create_task(simuliraj_temperaturu(30, True))
    moj_grad = VremenskaPrognoza("Pula", 6, datetime.now())
    await simuliraj_sljedecih_mjesec_dana(hladni_dani, moj_grad)

asyncio.run(main())
    

