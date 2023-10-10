primerNum=input("Introduce un número de teléfono con este formato: +00-000000000-00:")

# Dividir el número de teléfono en partes usando "-" como separador
partes = primerNum.split("-")

partUno=partes[0]
partDos=partes[1]
partTres=partes[2]

print("El número de teléfono principal es:", partDos)