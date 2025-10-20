#faktorijel broja

#koristeci for petlju
broj = int(input("Unesi broj: "))
broj2 = broj

if broj == 0:
    broj2 = 1

for i in range(1, broj2):
    broj2 = broj2 * i

print( broj, "! = " , broj2)

#koristeci while petlju
broj = int(input("Unesi broj: "))
broj2 = broj
i = 1

if broj == 0:
    broj2 = 1 

while i < broj:
    broj2 = broj2 * i
    i += 1
    
print( broj, "! = " , broj2)