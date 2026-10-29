tabla =[
    ["nombre","edad","calificacion"],
    ["luis",17,8.0],
    ["angel",16,9.0],
    ["joshua",16,7.0],
    ["danna",16,9.0],
    ["jorge",16,6.0],
    ["alma",16,9.0],
    ["santiago",17,7.0],
    ["keilani",16,6.0],
    ["angela",16,8.0],
    ["michel",16,8.0],
    ["aron",17,6.0]
]
nombre=input("introduce tu nombre:")

filas=len(tabla)
columnas=len(tabla[0])

for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
            print("posicion:"f" [{i}][{j}]") 
           