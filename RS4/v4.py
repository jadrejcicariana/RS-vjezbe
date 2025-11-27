#simulacija autentifikacije korisnika

import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

async def autentifikacija(username, password):

    #prvi dio zadatka:

    #await asyncio.sleep(2)
    #if korisnici[f"{username}"] == password:
        #print(f"{username} uspjesno prijavljen")
        #return True
    #else:
        #raise ValueError(f"{username}: neispravni podaci")
    
    #drugi dio zadatka:

    await asyncio.sleep(3)
    raise TimeoutError("ne radi servis")

        

async def main():
    
    r1 = asyncio.create_task(autentifikacija("korisnik1", "lozinka1"))
    r2 = asyncio.create_task(autentifikacija("korisnik2", "lozinka2"))
    r3 = asyncio.create_task(autentifikacija("korisnik2", "lozinka3"))
    r4 = asyncio.create_task(autentifikacija("korisnik3", "lozinka4"))
    r5 = asyncio.create_task(autentifikacija("korisnik3", "lozinka3"))

    try:
        await asyncio.wait_for(asyncio.gather(r1, r2, r3, r4, r5), timeout=4)
    except Exception as e:
        print("Dogodila se pogreska:", e)
    
    
asyncio.run(main())

#Kako se ponaša asyncio.gather() kada se dogodi
#iznimka u jednoj od korutina?
#gather ceka da se izvrse svi schedulani taskovi,
#i na kraju baci gresku na koju je prvu naisao