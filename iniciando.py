# import random
#
# numeroGanador=random.randint(1,10)
# numeroElegido=int(input('numero : '))
#
# if numeroGanador == numeroGanador:
#     print('has ganado')
#
# print('el numero ganador es :{}'.format(numeroGanador))

    # programa


# edad = int(input("Ingrese su edad: "))
# tipoCarnet=input("E = estudiante , P = pensionista , F = familia numerosa ,  N = nada : ")
#
# # (edad > 25 and edad < 35 and tipoCarnet=="E")
#
# if (25 > edad < 35 and tipoCarnet=="E") or \
#     edad<10 or \
#     (edad>65 and tipoCarnet=="P") or \
#     (tipoCarnet=="F"):
#     print("Se aplica el descuento")
# else:
#     print("No se te aplica el descuento")

"""la queseria xd"""

# titulo="Bienvenido al test sobre el queso"
# print("\n"+titulo+"\n"+"-"*len(titulo)+"\n")
#
# puntacion=0
#
# opcion=input("P1: Que haces cuando ves una tabla de queso ?\n"
#              "A- salgo corriendo \n"
#              "B- Pruebo uno de los quesos o incluso varios \n"
#              "C- No puedo evitar devorarla \n")
#
# if opcion=="A":
#     puntacion += 0
#
# elif opcion=="B":
#     puntacion += 5
#
# elif opcion=="C":
#     puntacion += 10
# else:
#     print("Las opcioes posibles son A,B,C")
#     exit()
#
# opcion=input("P2: como te gusta la hamburguesa ?\n"
#              "A- sin queso \n"
#              "B- con queso \n"
#              "C- pan y queso \n")
#
# if opcion=="A":
#     puntacion += 0
#
# elif opcion=="B":
#     puntacion += 5
#
# elif opcion=="C":
#     puntacion += 10
# else:
#     print("Las opcioes posibles son A,B,C")
#     exit()
#
# opcion=input("P3: Eres intolerante a la lactorsa ?\n"
#              "A- si \n"
#              "B- No lo se \n"
#              "C- no \n")
#
# if opcion=="A":
#     puntacion += 0
#
# elif opcion=="B":
#     puntacion += 5
#
# elif opcion=="C":
#     puntacion += 10
# else:
#     print("Las opcioes posibles son A,B,C")
#     exit()
#
#
# if puntacion<5:
#     print(f"No te agrada el queso :{puntacion}")
# elif 5>=puntacion<10:
#     print(f"TOLERAS el queso :{puntacion}")
# elif puntacion>=10:
#     print(f"Te ENCANTA el queso :{puntacion}")


# la casa de conversiones
# El usuario debe escojer que conversion debes hacer xd

dolarAeuro=0.91
libraAeuro=1.18

opcion=input("Escoja la conversion que desea realizar xd : \n"
             "A- dolar a euro \n"
             "B- Libra  a euro \n")

texto="Ingresa la cantidad {}"

if opcion == "A":
    print("Excelente estamos en la conversion de Dolar a euro")
    cantidadD=input("Ingresa la cantidad que desea convertir : \n")
    cantidadD=float(cantidadD)
    cantindadSalidaD=cantidadD*dolarAeuro
    print(f"Tus ${cantidadD} a €{cantindadSalidaD}")


elif opcion == "B":
    print("Excelente estamos en la conversion de Libra a euro :")
    cantidadL=float(input("Ingresa la cantidad que deseas convertir : \n"))
    cantidadSalidaL=cantidadL*libraAeuro
    print(f"Tus £{cantidadL} a €{cantidadSalidaL}")



















