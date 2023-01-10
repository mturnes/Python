print ("Ingrese las 3 notas para calcular la nota final: ")


print ("Nota 1:")
nota_1 = input()
print ("Nota 2")
nota_2= input()
print ("Nota 3")
nota_3 = input()

nota1= float (nota_1)*0.2
nota2= float (nota_2)*0.3
nota3= float (nota_3)*0.5

notafinal= float (nota1+nota2+nota3)

#notafinal= float ((nota_1*0.2)+(nota_2*0.3)+(nota_3*0.5))
print(notafinal)