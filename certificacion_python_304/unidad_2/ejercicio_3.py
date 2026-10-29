#Creando una matriz
abecedario=[
    ["a","b","c","d"],
    ["e","f","g","h"],
    ["i","j","k","l"],
    ["m","n","ñ","o"],
    ["p","q","r","s"],
    ["t","u","v","w"],
    ["x","y","z",""]
]
for i in range(0,7):#Fila<3
    #Ciclo interno para los indices de las columnas(j)
    for j in range(0,4):#Columna<3
        print(f"[{i}] [{j}] = {abecedario[i] [j]}")