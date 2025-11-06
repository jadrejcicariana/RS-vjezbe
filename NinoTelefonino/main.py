from data import pozivni


def validiraj_broj_telefona(broj: str):
    pozivni_broj = ""
    broj_ostatak = ""
    vrsta = ""
    mjesto = ""
    operater = ""
    validan = True

    novi_broj = ''.join(filter(lambda x: x.isdigit(), broj))

    if novi_broj.startswith("385"):
        novi_broj = novi_broj[3:]
    elif novi_broj.startswith("00385"):
        novi_broj = novi_broj[5:]
    else:
        validan = False
    
    novi_broj = '0'+novi_broj

    pronadjen = False

    for x in pozivni.keys():
       
        if (novi_broj.startswith(x) & (not pronadjen)):
            pronadjen = True
            pozivni_broj = x
            broj_ostatak = novi_broj[len(x):]
            vrsta = pozivni[x]["vrsta"]

            if vrsta == "fiksna mreza":
                if len(broj_ostatak) == 6 or len(broj_ostatak) == 7:
                    mjesto = pozivni[x]["mjesto_operater"]
                    operater = "None"
                else:
                    validan = False
            elif vrsta == "mobilna mreza":
                if len(broj_ostatak) == 6 or len(broj_ostatak) == 7:
                    mjesto = "None"
                    operater = pozivni[x]["mjesto_operater"]
                else:
                    validan = False
            else: 
                if len(broj_ostatak) == 6:
                    mjesto = "None"
                    operater = "None"
                else:
                    validan = False
            break

    if not pronadjen:
        validan = False         
           
    return {
        "pozivni_broj": pozivni_broj,
        "broj_ostatak": broj_ostatak,
        "vrsta": vrsta,
        "mjesto": mjesto,
        "operater": operater,
        "validan": validan
    }

print(validiraj_broj_telefona("+385 91 123 4567"))