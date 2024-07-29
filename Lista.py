
print("Bienvenido a la creacion de la lista de productos para comprar")
print("presiona enter para continuar \n")
producto=None

listaCompras = []

#while producto != "Q":
while True:
    producto = input("Que deseas comprar? (presiona 'Q' si deseas salir de la lista): ").upper()
    if producto=="Q":
        break
    if producto in listaCompras:
        print(f"{producto} ya se encuentra agregado")
    rpt=input(f"seguro que deseas comprar {producto}? [S/N]").upper()

    if rpt=="S":
        print(f"{producto} agregado!")
        listaCompras.append(producto)


print(f"En hora buena tu lista de compras se encuentra aqui: \n {listaCompras}")

# else:
#     print("")
