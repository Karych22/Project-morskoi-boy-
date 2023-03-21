try:
    print('Перед исключением')
    a = int(input('a: '))
    b = int(input('b: '))
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e)
    print('После исключения')

print('После после исключения')