coste=input("Coste en euros (Para determinar centimos use '.'): ")

parte=coste.split(".")
euro=parte[0]
centimos=parte[1]

print(f"Son {euro} euros y {centimos} centimos")