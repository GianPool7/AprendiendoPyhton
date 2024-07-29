import random

titulo="Bienvenido a pokemon"
rayas=len(titulo)

print("\n"+titulo+"\n"+"-"*rayas+"\n")

poder = random.randint(1, 3)
print(poder)

vidaPikachu=100
vidaSquirt=100

pokemon=input("Escoje tu pokemon \n"
      "A- pikachu \n"
      "B- squirt \n")

texto="En hora buena has escojido a {}"
batalla="Tendras una batalla epica con {}"
vida="tu vida es de {}"
danio="La vida del enemigo ha bajado a {}"
danioRecibido="Tu vida ha sido reducida a {}"

barraM = vidaPikachu * "#"
barraE = vidaPikachu * "*"

if pokemon == "A":
    print(texto.format("Pikachu"))
    print(batalla.format("Squirt"))
    print(f"Pikachu [{barraM}] {vidaPikachu}")
    print(f"Squirt [{barraE}] {vidaSquirt}")
    while vidaSquirt>0 and vidaPikachu>0:
        poder=input("Tus poderes son : \n"
              "1- bola de voltio , 10 danio \n"
              "2- onda de trueno , 15 danio \n"
              "3- cola de hierro , 30 danio \n")

        if poder=="1" :
            vidaSquirt -= 10
            barraE=vidaSquirt*"#"
            print(f"la vida de Squirt :[ {barraE} ] {vidaSquirt}")
            poderE=random.randint(1,3)
            if poderE==1:
                vidaPikachu -= 10
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")
            elif poderE==2:
                vidaPikachu -= 13
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")
            elif poderE==3:
                vidaPikachu -= 25
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")

        elif poder=="2":
            vidaSquirt -=15
            barraE=vidaSquirt*"#"
            #print(f"la vida de Pikachu :[ {barraE} ] {vidaPikachu}")
            print(f"la vida de Squirt :[ {barraE} ] {vidaSquirt}")
            poderE = random.randint(1, 3)
            if poderE == 1:
                vidaPikachu -= 10
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")
            elif poderE == 2:
                vidaPikachu -= 13
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")
            elif poderE == 3:
                vidaPikachu -= 25
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")

        elif poder=="3":
            vidaSquirt -=30
            barraE=vidaSquirt*"#"
            print(f"la vida de Squirt :[ {barraE} ] {vidaSquirt}")
            poderE = random.randint(1, 3)
            if poderE == 1:
                vidaPikachu -= 10
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")
            elif poderE == 2:
                vidaPikachu -= 13
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")
            elif poderE == 3:
                vidaPikachu -= 25
                barraM = vidaPikachu * "#"
                print(f"la vida de Pikachu :[ {barraM} ] {vidaPikachu}")

    if vidaPikachu>vidaSquirt:
        print("Has ganado al enemigo")
    else:
        print("Has sido derrotado")


elif pokemon == "B":
    print(texto.format("Squirt"))
    print(batalla.format("Pikachu"))
    print(f"Pikachu [{barraM}] {vidaSquirt}")
    print(f"Squirt [{barraE}] {vidaPikachu}")
    while vidaPikachu>0 and vidaSquirt>0 :
        poder = input("Tus poderes son : \n"
                      "1- placaje , 10 danio \n"
                      "2- chorro de agua ,13 danio \n"
                      "3- burbuja , 25 danio \n")
        if poder=="1" :
            vidaPikachu -= 10
            barraE=vidaPikachu*"#"
            print(f"La vida de pikachu : [{ barraE }] {vidaPikachu}")
            poderE = random.randint(1, 3)
            if poderE == 1:
                vidaSquirt -= 10
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")
            elif poderE == 2:
                vidaSquirt -= 15
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")
            elif poderE == 3:
                vidaSquirt -= 30
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")

        elif poder=="2":
            vidaPikachu -=13
            barraE=vidaPikachu*"#"
            print(f"La vida de pikachu : [{barraE}] {vidaPikachu}")
            poderE = random.randint(1, 3)
            if poderE == 1:
                vidaSquirt -= 10
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")
            elif poderE == 2:
                vidaSquirt -= 15
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")
            elif poderE == 3:
                vidaSquirt -= 30
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")

        elif poder=="3":
            vidaPikachu -=25
            barraE=vidaPikachu*"#"
            print(f"La vida de pikachu : [{ barraE }] {vidaPikachu}")
            poderE = random.randint(1, 3)
            if poderE == 1:
                vidaSquirt -= 10
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")
            elif poderE == 2:
                vidaSquirt -= 15
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")
            elif poderE == 3:
                vidaSquirt -= 30
                barraM = vidaSquirt * "#"
                print(f"la vida de Squirt :[ {barraM} ] {vidaSquirt}")

    if vidaPikachu<vidaSquirt:
        print("Has ganado al enemigo")
    else:
        print("Has sido derrotado")
