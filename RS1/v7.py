#validacija i provjera jakosti lozinke

lozinka = input("Unesite lozinku: ")

def provjera_lozinke(lozinka):
    duljina = len(lozinka)
    sadrzi_veliko_slovo = False
    sadrzi_broj = False

    for znak in lozinka:
        if znak.isupper():
            sadrzi_veliko_slovo = True
        elif znak.isdigit():
            sadrzi_broj = True

    if duljina < 8 or duljina > 15:
        print("Lozinka mora sadrzavati izmedu 8 i 15 znakova.")
 
    elif not sadrzi_veliko_slovo or not sadrzi_broj:
        print("Lozinka mora sadrzavati barem jedno veliko slovo i jedan broj.")
    
    elif "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadrzavati rijeci 'password' ili 'lozinka'.")
    
    else:
        print("Lozinka je jaka.")

provjera_lozinke(lozinka)
