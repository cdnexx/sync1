numero = int(input("Ingrese un número: "))
numero = str(numero)
largo_numero = len(numero)

if(largo_numero>10):
    if (numero==numero[::-1]):
        print(f'{numero} Es capicua.')
    else:
        print(f'{numero} No es capicua.')

else:
    print('El número debe tener más de 10 dígitos.')
