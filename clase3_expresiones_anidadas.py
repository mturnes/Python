nombre = input ("Ingrese Nombre: ")
edad = int (input ("Ingrese Edad: "))

estado= nombre != "****" and edad > 5 and edad < 20 and len (nombre) >= 4 and len (nombre) <8 and edad*3 > 35
print(estado)
