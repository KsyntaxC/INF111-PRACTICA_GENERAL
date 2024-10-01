#Dada la velocidad en metros por segundo de despegue de un avion y la aceleracion en metros por segundo 
#se pide calcular el tamaño de la pista 
V=float(input("Introduce la velocidad en metros por segundo: "))
A=float(input("Introduce la Aceleracion en en metros por segundo: "))
D=(V**2)/(2*A)
print("Tamaño de la Pista: ",round(D, 3),"m")