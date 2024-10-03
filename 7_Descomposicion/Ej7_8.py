#Dado un numero N imprimir algun otro que tenga n digitos, sea multiplo de 3 y sea minimo.
N=int(input("Introduce el número de dígitos n: "))
n=10**(N-1)
if n%3!=0:
    n=n+(3-n%3)
print(n)