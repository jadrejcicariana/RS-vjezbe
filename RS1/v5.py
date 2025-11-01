#analiziraj for petlje

#zasto nema smisla?
for i in range(1, 2):
    print(i)
#jer se desna granica intervala ne uzima u obzir, samo jednom ulazi u petlju

#sto ce ispisati?
for i in range(10, 1, 2):
    print(i)
#nista jer krece od 10 s korakom 2, ne moze doci do 1

#sto ce ispisati?
for i in range(10, 1, -1):
    print(i)
#korak negativan, ide od 10 do 2
