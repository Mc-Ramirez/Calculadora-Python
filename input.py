first = input('Ingrese el primero numero: ')
try:
    first = int(first)
except:
    first = 'cadena'
if first == 'cadena':
    print('El valor ingresado no es un numero')
    exit()

second = input('Ingrese el segundo numero: ')
try:
    second = int(second)
except:
    second = 'cadena'
if second == 'cadena':
    print('El valor ingresado no es un numero')
    exit()


print(first + second)
