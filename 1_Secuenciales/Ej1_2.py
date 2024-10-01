#Escribe un programa que dado dos puntos con coordenadas (x1, y1) y (x2, y2) 
#Calcule la distancia D entre los dos puntos. Debe mostrar la salida con formato de 2 decimales.
x1=float(input("Introduce el valor de x1: "))
y1=float(input("Introduce el valor de y1: "))
x2=float(input("Introduce el valor de x2: "))
y2=float(input("Introduce el valor de y2: "))
D=((x2-x1)**2 + (y2-y1)**2)**0.5
print("La distancia entre los dos puntos es ",round(D, 2))