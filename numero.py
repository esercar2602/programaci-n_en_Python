num = int(input("Dime un número"))
if num > 0:
    print("positivo")
if num < 0:
    print("negativo")
if num == 0:
    print("No es ni negativo ni posiivo")



num =int(input("Dime un año"))
if num % 4 == 0 and num % 100 != 0:
    print("Es bisiesto")
elif num % 400 == 0:
    print("es bisiesto")
else:
    print("No es bisiesto")