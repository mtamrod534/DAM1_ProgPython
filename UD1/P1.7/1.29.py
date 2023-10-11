#PSEUDOCODIGO

#Inicio
    #lee nombre, edad
    #Si nombre=="" hacer
        #Escribe "Nombre desconocido"      
    #Sino hacer
        #Mientras edad<0 o edad>125 hacer
            #Escribe "Edad no válida"
            #lee edad

    #Hacer años=125-edad
    #Escribe "Te llamas {nombre} y tienes {edad} años, te quedan aún {años} años por cumplir"
#Fin

nombre=input("Introduce un nombre: ")
edad=int(input("Introduce una edad: "))

if nombre=="":
    print("Nombre desconocido")
    nombre="desconocido"

while edad<0 or edad>125:
    print("Edad no válida")
    edad=int(input("Introduce una edad: "))

años=125-edad

print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años} años por cumplir")

