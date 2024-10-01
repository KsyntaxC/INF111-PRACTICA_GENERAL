#Serie: 1, 8, 27, 64, 125, 216, ...
N=int(input("Intro N: "))
i=1; t=i**3
while i<N+1:
    print(t,end=", ")
    i=i+1; t=i**3
    