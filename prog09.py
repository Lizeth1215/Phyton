#Escriba un programa que pregunte al usuario cuántos números de Fibonacci generar
#y luego los genere. Aproveche esta oportunidad para pensar en cómo puede usar
#las funciones. Asegúrese de pedirle al usuario que ingrese el número de números
#en la secuencia que desea generar.

num=int(input("Ingresa la cantidad de numeros de Fibonacci que quieras generar: "))
pen=1
ult=1
print("\nLos primeros",num, "terminos de la sucesion de Fibonacci son: ")
if num==1:
    print(0)
elif num==2:
    print(0,1)
elif num==3:
    print(0,1,1)
else:
    print(0,1,1, end=" ")
    for i in range(num-3):
        nuevo=ult+pen
        print(nuevo, end=" ")
        pen=ult
        ult=nuevo

