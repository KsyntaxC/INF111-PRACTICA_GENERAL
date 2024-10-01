#Hallar el factorial de un número N
N=int(input("Intro N: "))
i=1; fac=1
while i!=N+1:
	fac=fac*i
	i=i+1
print(N,"! =",fac)