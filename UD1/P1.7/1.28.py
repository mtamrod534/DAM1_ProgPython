#PSEUDOCODIGO

#Inicio
    #lee numeroUno, numeroDos
    #Si numeroUno==numeroDos hacer
        #Escribe "ERROR, los números no pueden ser iguales"
    #Sino
        #Si numeroUno>numeroDos hacer
            #mayor=numeroUno
            #menor=numeroDos
        #Sino
            #mayor=numeroDos
            #menor=numeroUno

        #diferencia=mayor-menor
        #Escribe "El número menor es {menor} y la diferencia entre ellos es de {diferencia} números enteros."
#Fin

numeroUno=int(input("Introduce el primer número: "))
numeroDos=int(input("Introduce el segundo número: "))

if numeroUno==numeroDos:
    print("ERROR, los números no pueden ser iguales")
else:
    if numeroUno>numeroDos:
        mayor=numeroUno
        menor=numeroDos
    else:
        mayor=numeroDos
        menor=numeroUno

    diferencia=mayor-menor
    print(f"El número menor es {menor} y la diferencia entre ellos es de {diferencia} números enteros.")
