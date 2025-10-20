#prosti brojevi

#fja isprime koja prima cijeli broj i vraca true ako je prost, false ako nije
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(isPrime(7))  
print(isPrime(10))   

#fja koja prima dva argumenta start i end, i vraca listu svih prostih brojeva u tom rasponu

def primes_in_range(start, end):
    prosti = []
    for num in range(start, end):
        if isPrime(num):
            prosti.append(num)
    return prosti

print(primes_in_range(1, 10))