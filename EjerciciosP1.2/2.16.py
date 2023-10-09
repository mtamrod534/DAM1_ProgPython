precio_pan=3.49

nodia=int(input("NºBarras de pan vendidas que no son del día: "))
pnodia=(precio_pan-precio_pan*0.6)*nodia
print("El pan del día vale",precio_pan,"€, si no es del día se le aplica un descuento del 60% por lo tanto el coste final de todas las barras vendidas que no son del día es de",round(pnodia,2),"€")



