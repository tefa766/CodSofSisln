#Escribir un programa que capture el precio de una bicicleta y muestre los impuestos que debe pagar siguiendo los criterios siguientes:
# Costo					Impuesto
# >100000				15%
# >50000 y <= 100000	10% 
#<=50000				 5%

costo = int(input("Inserta el costo"))
if costo > 100000:
  impuesto = costo * 0.15
elif costo > 500000 and costo <= 100000:
    impuesto = costo * 0.10
else:
    impuesto = costo * 0.05
print("el impuesto a pagar es:", impuesto)