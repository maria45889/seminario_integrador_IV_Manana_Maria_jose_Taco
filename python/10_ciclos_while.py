poder = 2000
while poder < 10000:
    print("Vegeta esta entrenando")
    poder += 2000

print("Vegeta ha alcanzado su obetivo")

while poder >0:
    print("Majin Buy tiene", poder, "de poder")
    poder -= 500

print("Majin buu quedo sin energia")

print("Continue y Break")
dia = 0
while dia < 0:
    dia += 1
    if dia == 4:
        print("Dia 4: gohan estudia")
        continue
    print("Dia", dia, "Gohan entrena")
    if dia == 8:
        print("DFin del sistema ")
        break