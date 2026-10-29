
try:
    alumnos=["danna","joshua","jaramillo","santiago","michelle"]
    calificaciones=[9,8,10,6,7]

    print(alumnos[0], calificaciones[0])
    print(alumnos[2], calificaciones[2])
    print(alumnos[4], calificaciones[4])

except IndexError:
    print("hay un error")
