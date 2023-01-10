


#g_silenciosa =   #1920/1940
#baby_boomer =  #1946/1964
#gen_x =      #1965/1979
#gen_y =         #1980/2000
#gen_z =        #2001/2010

comparador = int (input("Ingrese el año: "))
print (("Año Ingresado: "),comparador)

if comparador >= 1920 and comparador <= 1940:
    print ("Usted pertenece a la GENERACION SILENCIOSA")
elif comparador >= 1946 and comparador <= 1964:
    print ("Usted pertenece a la GENERACION BABY BOOMER")
elif comparador >= 1965 and comparador <= 1979:
    print ("Usted pertenece a la GENERACION X")
elif comparador >= 1950 and comparador <= 2000:
    print ("Usted pertenece a la GENERACION Y")
elif comparador >= 2000 and comparador <= 2010:
    print ("Usted pertenece a la GENERACION X")
else:
    print ("No existe generacion asociada")
