#Tome la lista L = [6, -2, 1, 1, -2, 3, 5, -8, 13, 21, -34, -55, 89] y
#escriba un programa que
#imprima todos los elementos de la lista que sean menores que 5.

L = [6, -2, 1, 1, -2, 3, 5, -8, 13, 21, -34, -55, 89]
print("Dada la siguiente lista de numeros\n",L,"\n")
print("De la lista de numeros, estos son los numeros < 5: ")
for i in L:
    if i<5:
        print(i)
