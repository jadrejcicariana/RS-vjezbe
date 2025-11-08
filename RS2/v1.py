#lambda izrazi
#lambda arguments : expression

#kvadriranje broja
print((lambda x : x ** 2)(5))

#zbroji pa kvadriraj
print((lambda x, y : (x + y) ** 2)(5, 2))

#kvadriraj duljinu niza
print((lambda x : len(x) ** 2)([1,2,3]))

#pomnozi vrijednost s 5 pa potenciraj na x
print((lambda x, y : (y * 5) ** x)(2, 3))

#vrati true ako je broj paran, inace none
#lambda arguments : expression if condition else expression
print((lambda x : True if x % 2 == 0 else None)(2))

