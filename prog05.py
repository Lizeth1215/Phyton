#Tome las listas L = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] y
#M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13] y escriba un programa que
#devuelva una lista que contenga solo los elementos que son comunes entre las listas (sin duplicados)

L = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13]

L.pop(1)
#print(L)
for i in L:
    for j in M:
        if i==j:
            print(i)

