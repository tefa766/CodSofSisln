#Escribir un programa que acepte el porcentaje de un alumno y evalue el grado de acuerdo al siguiente criterio 

#Calificacion Grado

#  >90          A
#  >80 y <= 90  B
#  >=60 y <=80  C
#  menor a 60   D

porcentaje = int(input("Inserta tu porcentaje" ))
if porcentaje >90:
   print("Grado: A")
elif porcentaje >80 and porcentaje <=90:
    print("Grado: B")
elif porcentaje >=60 and porcentaje <=80:
    print("Grado: C")
else:
    print("Grado: D")