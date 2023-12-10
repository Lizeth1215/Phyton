#Supongamos que se tiene una lista guardada en una variable:
#a = [1, 4, 9, 16, 25, 36, 49,64, 81, 100]. Escriba un programa que tome esta
#lista y haga una nueva lista que tenga solo los elementos pares de esta lista.

a = [1, 4, 9, 16, 25, 36, 49,64, 81, 100]
i=0
j=0
print("Los elementos de la lista son: ")
while i<len(a):
    print(a[i])
    i+=1
print("\nLa nueva lista, con solo los elementos pares de la lista son: ")
while j<len(a):
    if a[j]%2==0:
        print(a[j])
    j+=1

    
