#Dados tres interruptores se pide especificar el tipo de conexion para luego determinar si el circuito conduce o no corriente.
#La entrada consiste en una cadena ”paralelo.o ”serie”, que indica el tipo de conexion 
#y numeros a,b,c que son el estado de los interruptores que tomaran los valores de 0 o 1
tp=input("Ingrese el tipo de conexión ('paralelo' o 'serie'): ").strip().lower()
a=int(input("Digite 1 o 0: "))
b=int(input("Digite 1 o 0: "))
c=int(input("Digite 1 o 0: "))
if tp=="serie":
    if a==1 and b==1 and c==1:
        print("encendido")
    else:
        print("apagado")
elif tp=="paralelo":
    if a==1 or b==1 or c==1:
        print("encendido")
    else:
        print("apagado")
else:
    print("Tipo de conexión no válido.")