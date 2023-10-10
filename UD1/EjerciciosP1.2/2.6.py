importeFinal=float(input("Introduce el importe final: "))
ivaPagado=importeFinal*0.1
importeNoIva=importeFinal-ivaPagado

print("El iva pagado es", ivaPagado,"€ y el precio sin iva es", importeNoIva,"€")