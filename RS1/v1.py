#kalkulator

num1 = float(input('unesi prvi broj: '))
num2 = float(input('unesi drugi broj: '))
op = input('unesi operator (+, -, *, /): ')

if op == '+':
    res = num1 + num2
elif op == '-':
    res = num1 - num2
elif op == '*':
    res = num1 * num2
elif op == '/':
    if num2 == 0:
        print('dijeljenje s nulom nije dozvoljeno')
    res = num1 / num2
else:
    print('nepodrzani operator')

print('rezultat operacije ', num1, op, num2, 'je', res)