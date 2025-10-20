#brojanje rijeci u tekstu

tekst = "Python je programski jezik koji je jednostavan za ucenje i koristenje. Python je vrlo popularan"

def brojanje_rijeci(tekst):
    
    rijeci = tekst.split()

    return dict((rijec, rijeci.count(rijec)) for rijec in rijeci)

print(brojanje_rijeci(tekst))