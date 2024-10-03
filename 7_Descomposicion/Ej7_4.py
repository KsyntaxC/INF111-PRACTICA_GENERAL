#Dado un numero n crear dos nuevos numeros
#En el primero estaran digitos mayores que 5
#En el segundo los menores o iguales 5.
import math
n=int(input("Introduce el numero: "))
M=0; m=0; cd=int(math.log10(n))+1
while n!=0:
    d=n//10**(cd-1)
    n=n%10**(cd-1)
    cd=cd-1
    if d>5:
        M=M*10+d
    else:
        m=m*10+d
print(M)
print(m)