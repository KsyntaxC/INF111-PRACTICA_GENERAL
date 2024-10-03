#En este ejercicio decimos que un numero es balanceado si la suma de sus
#dıgitos en posiciones pares es igual a la suma de sus dıgitos en posiciones impares. (Si notamos en particular para este problema, 
# da igual si contamos las posiciones de izquierda a
#derecha o de derecha a izquierda). Nota: usar descomposicion de numeros.
#Entrada: La entrada consiste de multiples casos de prueba. Cada caso de prueba es un
#numero entero positivo. Termina cuando no hay mas datos.
n=int(input("Intro N: "))
i=1; x=0; y=0
while n!=0:
    d=n%10; n=n//10
    if i%2==0:
        y=y+d
    else:
        x=x+d
    i=i+1
if x==y:
    print("SI")
else:
    print("NO")