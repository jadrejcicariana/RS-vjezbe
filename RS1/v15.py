#pobroji samoglasnike i suglasnike

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

string = "Python je programski jezik koji je jednostavan za ucenje i koristenje. Python je vrlo popularan."

def count_vowels_consonants(string):

    rjecnik = {"vowels": 0, "consonants": 0}

    for char in string:
        if char in vowels:
            rjecnik["vowels"] += 1
        elif char in consonants:
            rjecnik["consonants"] += 1

    return rjecnik

print(count_vowels_consonants(string))