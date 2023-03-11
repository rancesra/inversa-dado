# inversa dado

numerodado = int(input("escriba el numero de la cada del dado: "))


#validacion

if(numerodado == 6):
    rta = "la inversa de " + numerodado + "es 1"
elif(numerodado == 5):
    rta = "la inversa de " + numerodado + "es 2"
elif(numerodado == 4):
    rta = "la inversa de " + numerodado + "es 3"
elif(numerodado == 3):
    rta = "la inversa de " + numerodado + "es 4"
elif(numerodado == 2):
    rta = "la inversa de " + numerodado + "es 5"
elif(numerodado == 1):
    rta = "la inversa de " + numerodado + "es 6"
else:
    rta = ("inserte un numero de 1 a 6")
    
print(str(rta)) 