#Serie: 1 1 1 2 1 2 3 2 6 4 5 24 5 8 120 6 13 720 ...
N=int(input("Intro N: "))
i=1; fac=1; a=1; b=0; fibo=a+b
while i!=N:
    print(i,end=" ")
    if fibo%3!=0:
        print(fibo,end=" ")
    else:
        a=b; b=fibo; fibo=a+b
        print(fibo,end=" ")
    print(fac,end=" ")
    i=i+1
    a=b; b=fibo; fibo=a+b
    fac=fac*i
    