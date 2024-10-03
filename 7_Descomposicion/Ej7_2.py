#Descripcion: Se te dara un numero x y tu tarea es rotar sus dıgitos n veces a la izquierda.
#Entrada: La entrada consiste en T casos de prueba, para cada caso se te dara dos numeros
#enteros x y n.
#Salida: La salida deberia ser el numero x rotado n veces a la izquierda
T=int(input("Introduce el número de casos de prueba: "))
i=0
while i<T:
    x=int(input("Introduce el numero de x: "))
    n=int(input("Introduce el numero de rotaciones: "))
    cd=0; t=x
    while t>0:
        cd=cd+1
        t=t//10
    n=n%cd
    j=0
    while j<n:
        pd=x//(10**(cd-1))
        x=x%(10**(cd-1))
        x=x*10+pd
        j=j+1
    i=i+1
    print(x)

