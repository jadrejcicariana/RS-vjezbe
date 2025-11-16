#korutina autentifikacija

import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]



async def autorizacija(user, lozinka):

    await asyncio.sleep(2)

    try:
        next(x for x in baza_lozinka if x["korisnicko_ime"] == user["korisnicko_ime"] and x["lozinka"] == lozinka)
    except:
        print(f"korisnik {user}: autorizacija neuspjesna")
        return None

    print(f"korisnik {user}: autorizacija uspjesna")
    

async def autentifikacija(korisnik):

    await asyncio.sleep(3)

    try:
        user = next((x for x in baza_korisnika if x["korisnicko_ime"] == korisnik["korisnicko_ime"] and x["email"] == korisnik["email"]))
    except:
        print(f"korisnik {korisnik} nije pronadjen")
        return None    
            
    await autorizacija(user, korisnik["lozinka"])

async def main():
    korisnik1 = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    await autentifikacija(korisnik1)

asyncio.run(main())