# 1 − 0 + 1 − 2 + 1 − 0 + 1 − 2 + 3 − 2 + 1 − 0 + 1 − 2 + 3 − 4 + 3 − 2 + 1 − 0 + 1 − 2 + 3 − 4 + 5 − 4.....
n=int(input("Intro n: "))
i=1; v=-1; t=1; b=1; a=0; s=0
while i<n+1:
    if i%2==0:
        s=s-t
    else:
        s=s+t
    t=t+v
    if t==a:
        v=v*(-1); b=b+1
    elif t==b:
        v=v*(-1)  
    i=i+1
print(s)