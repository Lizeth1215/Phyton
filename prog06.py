#Pídale al usuario una cadena e imprima si esta cadena es un palíndromo o no.

def palindromo(palabra):

    palabra=palabra.lower()
    palabra=palabra.replace(" ","")
    a=0;
    b=len(palabra)-1
    for i in range(0,len(palabra)):
        if palabra[a]==palabra[b]:
            a+=1
            b-=1
        else:
            return False
    return True
    

palabra=input("Ingrese una palabra o una frase: ")
if palindromo(palabra):
    print("Es una palabra o frase palindroma")
else:
    print("No es una palabra o frase palindroma")
