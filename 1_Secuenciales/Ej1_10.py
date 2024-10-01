#Dadas las horas, minutos y segundos se le pide sumar un segundo.
#La entrada consiste de 3 números enteros separados por un espacio que representan las horas minutos y segundos. 
#Donde horas < 24, minutos < 60 segundos < 60. 4
#Salida: Imprima en la salida la nueva hora del reloj en formato mostrado en el ejemplo.
#Las horas, minutos y segundos deben estar en el siguiente formato:
XX = int(input("Ingrese la hora (0-23): "))  
YY = int(input("Ingrese los minutos (0-59): "))
ZZ = int(input("Ingrese los segundos (0-59): "))
ZZ=ZZ+1
if ZZ==60:
    ZZ=0
    YY=YY+1
if YY==60:
    YY=0
    XX=XX+1
if XX==24:
    XX=0
print(f"{XX:02d}:{YY:02d}:{ZZ:02d}")
