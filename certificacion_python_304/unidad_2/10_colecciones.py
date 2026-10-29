carrito=[]#Lista vacia
n_productos=int(input("Ingresa el numero de productos:"))
for i in range(n_productos):
    producto=input("Ingresa el producto a ru carrito:")
    carrito.append(producto)
print("Lista creada correctamente")
carrito[0]="barritas"
print(f"Tu carrito contiene{carrito}")
print(carrito[0])
print(carrito[1])
