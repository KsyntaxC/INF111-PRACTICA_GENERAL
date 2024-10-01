#Hay tres hermanos llamados A, B y C. Las relaciones de edad entre ellos se dan mediante
#tres caracteres SAB, SAC, y SBC, que significan lo siguiente:
Sab = input("Ingrese la relación de A con B ('<' o '>'): ")
Sac = input("Ingrese la relación de A con C ('<' o '>'): ")
Sbc = input("Ingrese la relación de B con C ('<' o '>'): ")
if Sab == '<' and Sac == '>' and Sbc == '<':
    h_med = 'A'
elif Sab == '>' and Sac == '>' and Sbc == '>':
    h_med = 'B'
elif Sab == '<' and Sac == '<' and Sbc == '>':
    h_med = 'C'
elif Sab == '<' and Sac == '<' and Sbc == '<':
    h_med = 'B'
elif Sab == '>' and Sac == '<' and Sbc == '>':
    h_med = 'A'
elif Sab == '>' and Sac == '<' and Sbc == '<':
    h_med = 'C'
elif Sab == '<' and Sac == '>' and Sbc == '>':
    h_med = 'C'
elif Sab == '>' and Sac == '>' and Sbc == '<':
    h_med = 'A'
else:
    print("Ingrese los valores indicados")
print("El hermano mediano es:", h_med)