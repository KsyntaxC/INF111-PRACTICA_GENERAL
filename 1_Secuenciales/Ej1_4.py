#Dados un punto en coordenadas polares(r,θ) se pide que se haga su conversion a coordenadas rectangulares(x,y).
#Use la siguiente formula para la conversion a coordenadas rectangulares:
import math
r=float(input("Introduce la r: "))
θ=float(input("Introcuce la θ: "))
x = r*math.cos(θ)
y = r*math.sin(θ)
print("x: ",round(x, 3))
print("y: ",round(y, 3))