#PSEUDOCODIGO
#
#
#
#
#
#
#

num=int(input("Introduce el número: "))
incremento=int(input("Introduce el incremento: "))
total=int(input("Introduce el total: "))

while incremento<=0 or total<=0:
    print("Total e incremento deben ser mayor de 0")
    incremento=int(input("Introduce el incremento: "))
    total=int(input("Introduce el total: "))

while num<=total:
    print(num, end=", ")
    num+=incremento
