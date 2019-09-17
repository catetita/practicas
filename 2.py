print("programa de beca!")

distancia_escuela = int(input("ingresa la distancia de la escuela en km : "))
print(distancia_escuela)
cuantos_hermanos = int(input("cuantos hermanos tiene : "))
print(cuantos_hermanos)
salario_familiar = int(input("cual es el salario mensual en bruto : "))
print (salario_familiar)

if distancia_escuela > 40 and cuantos_hermanos > 1 and salario_familiar <= 20000:
    print("beca conseguida")
else:
    print("beca no conseguida")