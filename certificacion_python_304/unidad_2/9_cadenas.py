#cadenas y concatenacion(+)
cadena1='Hola '
cadena2='Mundo'
multilinea="""Esto es una cadena de varias lineas"""
print(cadena1 + cadena2 + multilinea)#print(f"{cadena1})
#cadenas y repeticion
eco="ja"*3
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='alma'
print(tu_nombre.upper())
#cambiar una cadena de mayuscula a minusculas
print(tu_nombre.lower())
#remplazar texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#Formato de cadenas(F-String)
edad=16
nombre='Alma'
mensaje=f"Hola me llamo \n{nombre}\ny tengo \n{edad} años"
print(mensaje)
#Contar los caracteres de una cadena
texto= "¡Felicidades por aun continuar en el cecy!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto contiene una palabra
oracion="apender python es divertido"
if "java" in oracion:
    print("encontrado")
else:
    print("No esta")
    #Validar contenido de una cadena
    nlista="alma"
    print(nlista.isalpha())
    print(nlista.isdigit())