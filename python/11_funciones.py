print("Funciones ")
print("Autor: Maria Jose Taco")

def kamehameha():
    print("Goku consentra su energia")
    print("!kamehameha")

kamehameha()
kamehameha()
kamehameha()
kamehameha()

def atacar(gueerrero):
    print(gueerrero, "realiza un ataque")

atacar("Goku")
atacar("Vegeta")
atacar("Piccolo")
atacar("Maria Jose Taco")

def calcular_poder(poder, ataques):
    danio = poder * ataques
    return danio

resultado = calcular_poder(4,26)
print("El poder de Maria Jose Taco es :", resultado)

resultado = calcular_poder(4,5000)
print("El poder de Goki es :", resultado) 

def tranformar_saiyajin(nombre, poder):
    if poder >=9000:
        print(f"Tranfomacion de {nombre} a SuperSaiyajin exitosa")
    else:
        print(f"{nombre} Necesita aumentar tu poder")

tranformar_saiyajin("Maria Jose Taco", 500)
tranformar_saiyajin("Gohan", 1500)

nombre_personaje: str = "Goku"
edad: int = 33
altura: float=1.74
es_activo: bool= True

def multiplicador_poder(entrenamiento: float, edad: int)->float:
    return entrenamiento*edad

poder:float = multiplicador_poder(15.5, 2)
print("Poder calculado ", poder)