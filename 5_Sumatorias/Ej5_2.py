#Sumatoria Patito Juez
# - 2*((x^1)/1) + 2*((x^2)/1) - 3*((x^2)/2) + 3*((x^3)/3) - 5*((x^3)/5) + 5*((x^3)/8) - 7*((x^4)/13) + 7*((x^4)/21) - ........
N=int(input("Intro N:"))
k=1
while k<N+1:
    n=int(input("Intro n: "))
    x=int(input("Intro x: "))
    i=1; s=0; p=2; pd=p; e=1; c=0; a=1; b=0; f=a+b; c3=1
    while i<n+1:
        if i%2==0:
            s=s+pd*((x**e)/f)
        else:
            s=s-pd*((x**e)/f)
        if c==2:
            p=p+1; c2=0; j=1
            while j<=p:
                if p%j==0:
                    c2=c2+1
                j=j+1
            if c2==2:
                pd=p
            c=1
        else:
            c=c+1  
        a=b; b=f; f=a+b; c=c+1
        if c3==e:
            e=e+1; c3=1
        i=i+1
    print("=", f"{s:.4f}")
    k=k+1