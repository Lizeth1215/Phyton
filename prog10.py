#Genere un número aleatorio entre 1 y 9 (incluyendo 1 y 9). Pídale al usuario que
#adivine el número, luego dígale si adivinó demasiado bajo, demasiado alto o
#exactamente correcto.

import random

numero=random.randint(1,9)
opcion=True
intentos=0
print("Adivina un numero entre 1 y 9: ")
while opcion:
    intentos+=1
    if intentos<=100:
        eleccion=int(input("Elige un numero: "))
        if eleccion==numero:
            print("¡Muy bien, adivinaste el numero! Has necesitado",intentos, "intentos")
            opcion=False
            break
        elif eleccion>numero:
            print("Demasiado alto, llevas",intentos,"intentos")
        elif eleccion<numero:
            print("Demasiado bajo, llevas",intentos, "intentos")
    else:
        opcion=False
              
        
              
