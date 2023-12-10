#Pídale al usuario un numero. Dependiendo si el numero sea par o impar,
#imprima un mensaje apropiado.

numero = int(input("Escriba un numero entero: "))
if numero % 2 == 0:
    print("El numero ",numero," es par")
else:
    print("El numero ",numero," es impar")
