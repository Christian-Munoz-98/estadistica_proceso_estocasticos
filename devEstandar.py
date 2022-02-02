from traceback import print_tb


datos = [13,15,18,21,21,21,22,22,24,28,28,37,40,43,50,55,66,68,70,74,74,78,79,83,83,87,89,90,93,95,96,98,98,102,103,112,112,115,118,120,121,124,132,135,158]
devEstandar = 0
N = len(datos)
media = 0

for observacion in datos:
    media+=observacion
media /= N

for observacion in datos:
    devEstandar+=(observacion-media)**2

devEstandar/=N
devEstandar**=0.5
print(devEstandar)


