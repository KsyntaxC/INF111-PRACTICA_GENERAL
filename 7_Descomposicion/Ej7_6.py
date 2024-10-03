#Dado un numero x llevar los dıgitos primos al inicio del numero si el numero es impar, en el
#caso de que el numero sea par llevar a los numeros primos al final del numero.
N=int(input("Introduce el número de dígitos n: "))
n=10**(N-1)
if n%3!=0:
    n=n+(3-n%3)
print(n)

