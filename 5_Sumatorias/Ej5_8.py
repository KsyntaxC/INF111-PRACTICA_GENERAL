#S = 2 − 3 + 5 − 7 + 11 − 13 + 17 − 19 + 23 − 29 + 31 + ...
n=int(input("intro n: "))
i=0; c=2; p=2; s=0
while i<n:
    if p%c!=0 and c<=p//2:
        c=c+1
    else:
        if c>p//2:
            if i%2==0:
                s=s+p
            else:
                s=s-p
            i=i+1
        p=p+1; c=2
print("=",s)