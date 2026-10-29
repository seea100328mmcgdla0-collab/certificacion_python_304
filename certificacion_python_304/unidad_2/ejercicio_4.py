#El mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","x","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#Recorriendo la matriz con ciclos anidados
#Ciclo extremo para manejar filas(i)
for i in range(filas):
    #Ciclo extremo para manejar columnas(j)
    for j in range(columnas):
        #verificamos si encontramos el tesoro
        if mapa[i][j]=="x":
            print(f"Mapa encontrado en la posicion [{i}][{j}]") 
