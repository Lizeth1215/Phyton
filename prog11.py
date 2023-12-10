#Escriba un programa que imprima (a + b)^n para cualquier n indicado por el usuario.

def calcu(a, b, n):
    resultado = (a + b) ** n
    return resultado

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
n = int(input("Ingrese el valor de n: "))

resultado = calcu(a, b, n)
print("\n(a + b)^n =", resultado)
