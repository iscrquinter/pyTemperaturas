#Temperaturas.py -- Temperaturas usando Tuples
import os
os.system("cls")

print("Temperaturas de la semana")
print("=========================")

temp=(15, 17, 15, 18, 15)

print("DIA  TEMPERATURA")
print("----------------")
print("Lunes     " + str(temp[0]))
print("Martes    " + str(temp[1]))
print("Miercoles " + str(temp[2]))
print("Jueves    " + str(temp[3]))
print("Viernes   " + str(temp[3]))
print("-----------------")

pt = sum(temp)/len(temp)

print("Promedio de temperatura en la semana=> " + str(pt))

if int(pt) in temp:
    print("El día " + temp.index(int(pt))+" coincidió con el promedio de temperatura de la semana ...")
else:
    print("Ningun día de la semana coincidió con el promedio de la semana ...")

print("La temperatura máxima fue->" + str(max(temp)) + " Y se tuvo " + str(temp.count(max(temp)))  + " dias ...")
print("La temperatura minima fue->" + str(min(temp)) + " Y se tuvo " + str(temp.count(min(temp)))  + " dias ...")
