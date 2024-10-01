#Dado un número n, Ordenar los dígitos en orden descendente.
#La entrada consiste de cinco 
#números enteros a,b,c,d,e. El objetivo es ordenarlos de mayor a menor
n=int(input("Ingrese un numero de 5 digitos: "))
a=n//10000
b=(n//1000)%10
c=(n//100)%10
d=(n//10)%10
e=n%10
if a>b:
    m1=a; m2=b
else:
    m1=b; m2=a
if c>m1:
    m3=m2; m2=m1; m1=c
else:
    if c<m2:
        m3=c
    else:
        m3=m2
        m2=c
if d>m1:
    m4=m3; m3=m2; m2=m1; m1=d
else:
    if d<m3:
        m4=d
    else:
        if d>m2:
            m4=m3; m3=m2; m2=d
        else:
            m4=m3; m3=d
if e>m1:
    m5=m4; m4=m3; m3=m2; m2=m1; m1=e
else:
    if e<m4:
        m5=e
    else:
        if e>3:
            m5=m4; m4=m3; m3=e
        else:
            if e>2:
                m5=m4; m4=m3; m3=m2; m2=e
            else:
                m5=m4; m4=e
print(m1,m2,m3,m4,m5)