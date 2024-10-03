#Ingresado un número N(1 ≤ N ≤ 100), iniciar con la prueba de números y dar pistas
#Acerca de que tan cerca se esta de N, finalizar el programa cuando se haya llegado a N.
N=int(input("Intro N: "))
x=int
while x != N:
	x=int(input("Introduzca prueba de números: "))
	if x>N:
		print ("El número es menor")
	if x<N:
		print("El número es mayor")
print("Número encontrado")