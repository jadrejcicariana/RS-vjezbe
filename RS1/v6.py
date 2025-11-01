#suma svih parnih brojeva od 1 do 100 (ukljucivo)
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print("suma svih parnih brojeva od 1 do 100 je: ", sum)

#prvih 10 neparnih u obrnutom redoslijedu
list = []
num = 1 

while len(list) < 10:
    list.append(num)
    num += 2

list.reverse()
print(list)
    

#fibonaccijev niz do 1000
a = 0
b = 1

while True:
    c = a + b
    if c > 1000:
        break
    print(c)

    a = b
    b = c