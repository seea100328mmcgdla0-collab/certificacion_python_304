#creando un diccionario
persona= {
    "Nombre":"Alma",
    "Edad":16,
    "Profesion":"Programador",
    "Estudiante":True
}
print(persona)
#Accediendo a un valor en especifico
print(persona["Nombre"])
#Se puede usar el metodo get()
#Es util porque no marca error si el valor no existe
print(persona.get("Profesion"))
#Modificar un valor existente
persona["Edad"]=20
print(persona["Edad"])