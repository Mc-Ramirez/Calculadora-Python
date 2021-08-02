nombre = input('Ingrese un nombre: ')
listaNombres = ['Francisco', 'Roberto', 'Felipe', 'Ana', 'Laura']
if listaNombres.count(nombre) > 0:
    print('El nombre', nombre, 'si esta guardado')
else:
    print('El nombre no esta guardado')
