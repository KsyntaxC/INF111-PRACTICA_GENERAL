#Serie: 1, 0, 3, 0, 0, 0, 5, 0, 0, 0, 0, 0, 7, 0, ...
N=int(input("Intro N: "))
i=0; im=1; ceros=0; c=0
while i<N:
    print(im,end=", ")
    while c<im:
        print(ceros,end=", ")
        c=c+1
    im=im+2
    c=0
    i=i+1
