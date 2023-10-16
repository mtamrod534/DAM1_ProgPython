# Ejercicio 1.33 - Lee 3 números y dame los números ordenados de menor a mayor.

# > Dame 3 números:
# > 14
# > 7
# > 10
# > Tus números son 7 10 14

# --------------------------------------------

# PSEUDOCÓDIGO

#Inicio

#	Escribe "Dame 3 números: "
#	Lee n1
#	Lee n2
#	Lee n3
	
#	Si (n1 < n2 and n1 < n3) entonces
#		Si (n2 < n3) entonces
#			Escribe n1 + " " + n2 + " " + n3
#		Sino
#			Escribe n1 + " " + n3 + " " + n2
#	Sino
#		Si (n2 < n1 and n2 < n3) entonces
#			Si (n1 < n3) entonces
#				Escribe n2 + " " + n1 + " " + n3
#			Sino
#				Escribe n2 + " " + n3 + " " + n1
#		Sino
#			Si (n3 < n1 and n3 < n2) entonces
#				Si (n1 < n2) entonces
#					Escribe n3 + " " + n1 + " " + n2
#				Sino
#					Escribe n3 + " " + n2 + " " + n1

#Fin

# --------------------------------------------

# PSEUDOCÓDIGO CORREGIDO

# Inicio

#	Escribe "Dame 3 números: "
#	Lee n1
#	Lee n2
#	Lee n3
	
#	Si (n1 < n2 and n1 < n3) entonces
#		Si (n2 < n3) entonces
#			Escribe n1 + " " + n2 + " " + n3
#		Sino
#			Escribe n1 + " " + n3 + " " + n2
#	Sino si (n2 < n1 and n2 < n3) entonces
#		Si (n1 < n3) entonces
#			Escribe n2 + " " + n1 + " " + n3
#		Sino
#			Escribe n2 + " " + n3 + " " + n1
#	Sino si (n3 < n1 and n3 < n2) entonces
#		Si (n1 < n2) entonces
#			Escribe n3 + " " + n1 + " " + n2
#		Sino
#			Escribe n3 + " " + n2 + " " + n1

# Fin

# --------------------------------------------

n1=int(input("Introduce un número: "))
n2=int(input("Introduce otro número: "))
n3=int(input("Introduce otro número más: "))

if (n1<n2) and (n1<n3):
    if (n2<n3):
        print(n1," ",n2," ",n3)
    else:
        print(n1," ",n3," ",n2)
elif (n2<n1) and (n2<n3):
    if (n1<n3):
        print(n2," ",n1," ",n3)
    else:
        print(n2," ",n3," ",n1)
elif (n3<n1) and (n3<n2):
    if (n1<n2):
        print(n3," ",n1," ",n2)
    else:
        print(n3," ",n2," ",n1)

