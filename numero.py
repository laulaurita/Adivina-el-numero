# un programa para generar y adivinar un numero dado
from random import*

#input
Eleccion = int(input("porfavor ingrese un numero de 1-100 : "))

#procesing and ouput
X = randint(1,100)

if X == Eleccion:
    Numerofinal = X
    print("Has acertado el numero", Numerofinal,)
elif X > Eleccion:
    Numerofinal = X
    print("el numero",Numerofinal,"es mayor al numero ingresado",Eleccion)
else:
    Numerofinal = X
    print("el numero",Numerofinal,"es menor al numero ingresado",Eleccion)