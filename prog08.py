#Haga un juego de piedra-papel-tijeras contra el ordenador. (Recuerde las reglas:
#la roca vence a las tijeras. Las tijeras superan al papel. El papel vence a la roca.)

while True:
    x=int(input("Jugador 1: 1=roca, 2=papel, 3=tijera: "))
    y=int(input("Jugador 2: 1=roca, 2=papel, 3=tijera: "))

    if x==1 and y==1:
        print("¡Empate!, va de nuevo")
    elif x==2 and y==2:
        print("¡Empate!, va de nuevo")
    elif x==3 and y==3:
        print("¡Empate!, va de nuevo")
    elif x==1 and y==3:
        print("¡Jugador 1 gana: roca vence tijera!")
    elif x==1 and y==2:
        print("¡Jugador 1 gana: roca vence papel!")
    elif x==2 and y==1:
        print("¡Jugador 1 gana: papel vence roca!")
    elif x==2 and y==3:
        print("¡Jugador 2 gana: tijera vence papel!")
    elif x==3 and y==2:
        print("¡Jugador 1 gana: tijera vence papel!")
    elif x==3 and y==1:
        print("¡Jugador 2 gana: roca vence tijera!")

    
        
