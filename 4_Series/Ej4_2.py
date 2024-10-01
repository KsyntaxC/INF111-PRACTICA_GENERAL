#Serie: 1 2 3 4 5 4 3 2 1 2 3 4 5 4 3 2 1 2 3 ...
#Resolver la siguiente secuencia para n términos. (sube y baja)
n=int(input("intro n terminos: "))
c=0; t=1; v=1; i=1
while i <= n:
    print(t,end=" ")
    t=t+v; c=c+1
    if c==4:
        v=v*(-1); c=0
    i=i+1