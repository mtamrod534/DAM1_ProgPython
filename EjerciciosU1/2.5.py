importeNoIVa=float(input("Introduce un importe sin IVA: "))
tipoIVA=str(input("Indica un tipo de iva (general, reducido o super_reducido): "))

if tipoIVA=="general":
    IVAgeneral=importeNoIVa-(0.21*importeNoIVa)
    print("El importe con el 21% es:", IVAgeneral, "€")
elif tipoIVA=="reducido":
    IVAreducido=importeNoIVa-(0.1*importeNoIVa)
    print("El importe con el 10% es:", IVAreducido, "€")
else :
    IVAsuperReducido=importeNoIVa-(0.04*importeNoIVa)
    print("El importe con el 4% es:", IVAsuperReducido, "€")
