#primera parte: fin de semana
n=0
fecha=""
tb=5
costtal=0
n=int(input("ingresa la cantidad de boletas a comprar: "))
fecha=input("la boleta es para fin de semana? (si o no): ")
if fecha=="si":
  costtal=tb*1.20
else:
  costtal=tb
print("el costo total a pagar", costtal*n)
#segunda parte
palco=""
palco=input("La boleta es para cual palco? (a, b ó c): ")
if palco=="a":
  costtal=costtal + tb*.1
elif palco =="b":
  costtal=costtal + tb*.05

print("el costo total con palco es: ", costtal*n)
#tercera parte

if n>5 and n<=10:
  costtal=costtal*.9
elif n>15 and n<=20:  
  costtal=costtal*.85
elif n >= 25:
  costtal=costtal*.80
print("El valor total a pagar es: ", round(costtal*n,2))