num = int(input("Dime la cantidad de segundos que quieras transformar"))
minutos = num // 60
segundos = num % 60

horas = minutos//60
minutos  = minutos % 60

print(horas, "h", minutos, "m", segundos, "s")



precio = float(input("Dime el precio de compra"))
porcentaje = int(input("Dime el porcentaje de beneficio"))
IVA = int(input("Dime el porcentaje de IVA"))
a = precio*(porcentaje/100)
b = precio + a 
c = b*(IVA/100)
precio_final = b + c
print(precio_final, "euros")
