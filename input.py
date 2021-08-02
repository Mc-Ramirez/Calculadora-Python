first = input('Ingrese el primero numero: ')
try:
    first = int(first)
except:
    first = 'cadena'

second = input('Ingrese el segundo numero: ')
try:
    second = int(second)
except:
    second = 'cadena'

if first == 'cadena' or second == 'cadena':
    print('Ingresaste mal los dos o uno de los datos, prueba otra vez y solo con numeros')
else:
    print(first + second)
