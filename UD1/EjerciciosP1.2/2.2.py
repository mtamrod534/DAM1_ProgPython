horas=float(input("Introduce las horas de trabajo: "))
coste=float(input("Introduce el coste del trabajo por hora: "))
servicio=horas*coste
round (servicio, 2)
print("Importe total:", servicio, "€")