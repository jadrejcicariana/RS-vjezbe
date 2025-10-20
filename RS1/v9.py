#uklanjanje duplikata iz liste

lista = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

def ukloni_duplikate(lista):
    return list(set(lista))

print(ukloni_duplikate(lista))


#implementacija pomocnim skupom
def ukloni_duplikate2(lista):
    
    lista2 = []
    
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    return lista2

print(ukloni_duplikate2(lista))