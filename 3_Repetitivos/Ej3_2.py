#Dado un número N, halle la suma de los números pares e impares
N=int(input("Intro N: "))
SP=2; SI=1
for i in range (3,N+1):
	if i%2==0:
		SP=SP+i
	else:
		SI=SI+i
print("La suma de pares es: ", SP)
print("La suma de impareses:",SI)