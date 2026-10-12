print("Operadores en Python")
print("Operadores Aritméticos")

a = 10
b = 5
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

print("tabla de multiplicar del 5")
print("5 x 1 =", 5 * 1)
print("5 x 2 =", 5 * 2)
print("5 x 3 =", 5 * 3)
print("5 x 4 =", 5 * 4)
print("5 x 5 =", 5 * 5)
print("5 x 6 =", 5 * 6)
print("5 x 7 =", 5 * 7)
print("5 x 8 =", 5 * 8)
print("5 x 9 =", 5 * 9)
print("5 x 10 =", 5 * 10)

print("Operadores de comparación")
print("Igual:", a == b)
print("Distinto:", a != b)
print("Mayor que :", a > b)
print("Mayor o igual:", a >= b)
print("Menor que :", a < b)
print("Menor o igual:", a <= b)

print("Mayor o igual:", a >= b)
print("Menor o igual:", a <= b)


print("Operadores lógicos")
print("AND:", a > 5 and b < 10)
print("OR:", a > 5 or b < 10)
print("NOT:", not(a > 5))

tiene_dinero = True
tiene_abierta = False

puede_comprar = tiene_dinero and tiene_abierta
print("Puede comprar:", puede_comprar)

es_cliente_vip = True
tiene_dinero = False
acceso_credito = es_cliente_vip or tiene_dinero
print("Acceso a crédito:", acceso_credito)
