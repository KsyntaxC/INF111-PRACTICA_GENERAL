#La entrada consiste de m´ultiples casos de prueba. 
#Para N mostrar en pantalla de la siguiente manera:
#N=3:
# 1 0 1
# 0 1 0 
# 1 0 1     
N=int(input("Introduce N: "))
i=0
while i < N:
    j=0
    while j<N:
        if (i+j)%2==0:
            print(1, end=" ")
        else:
            print(0, end=" ")
        j=j+1
    print()
    i=i+1
