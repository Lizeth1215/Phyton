#Cree un programa que solicite al usuario un número y luego imprima una lista
#de todos los divisores de ese número.

numero=int(input("Ingrese un número: "))
cont=0
print("\nLos divisores de",numero, "son: ")
for i in range(1,numero+1):
    if numero%i==0:
        print(i)
        cont=cont+1
#print("Los divisores de",numero, "son: ",i)
print("\nEl numero de divisores de",numero," es",cont)
