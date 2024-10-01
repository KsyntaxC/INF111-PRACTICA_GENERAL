#Serie: 2 7 17 34 62 103 161 238 338 467 ...
N=int(input("Intro N: "))
i=0; p=3; a=2; t=0; b=0; j=1; c=0
while i<N:
    t=t+a
    print(t,end=" ")
    while j<=p:
        if p%j==0:
            c=c+1
        c=0
        j=j+1
    if c==2:
        b=p
    p=p+1
    a=a+b
    i=i+1