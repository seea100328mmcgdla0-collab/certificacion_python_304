promedio=float(input("ingresa tu promedio:"))
#El numero ingresado es 9
if promedio<0:
    print("ese numero es invalido")
elif promedio<=5:
    print("Tu promedio es muy bajo")
elif promedio>5 and promedio<=6:
    print("Tu promedio es bajo")
elif promedio>7 and promedio<=9:
    print("Tu promedio es bueno")
elif promedio>9 and promedio<=10:
    print("tu promedio es excelente")
else:
    print("Ese promedio no existe")