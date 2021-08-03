first = input('Enter a number: ')
try:
    first = int(first)
except:
    first = 'string'
if first == 'string':
    print('The value entered is not a number')
    exit()

second = input('Enter a number: ')
try:
    second = int(second)
except:
    second = 'string'
if second == 'string':
    print('The value entered is not a number')
    exit()

symbol = input('Type the symbol of the operation you want to perform: ')
if symbol == '+':
    print('Suma: ', first + second)
elif symbol == '-':
    print('Resta: ', first - second)
elif symbol == '/':
    print('Divide: ', first / second)
elif symbol == '*':
    print('Multiplica: ', first + second)
elif symbol == '%':
    print('Resto: ', first % second)
else:
    print('Esta operacion no puede realizarse o no existe')
