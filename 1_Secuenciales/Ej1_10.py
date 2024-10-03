#Dadas las horas, minutos y segundos se le pide sumar un segundo.
#La entrada consiste de 3 números enteros separados por un espacio que representan las horas minutos y segundos. 
#Donde horas < 24, minutos < 60 segundos < 60. 4
#Salida: Imprima en la salida la nueva hora del reloj en formato mostrado en el ejemplo.
#Las horas, minutos y segundos deben estar en el siguiente formato:
XX = int(input("Ingrese la hora: "))  
YY = int(input("Ingrese los minutos: "))
ZZ = int(input("Ingrese los segundos: "))
TS=XX*3600+YY*60+ZZ+1
h=TS//3600%24
m=TS//60%60
s=TS%60
print(f"{h:02d}:{m:02d}:{s:02d}")