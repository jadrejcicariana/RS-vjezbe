#uklanjanje duplikata iz liste

lista = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

def ukloni_duplikate(lista):
    return list(set(lista))

print(ukloni_duplikate(lista))
