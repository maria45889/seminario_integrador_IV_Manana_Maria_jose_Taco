print("Operadores en el consultorio veterinario")

costo_consulta = 25
costo_vacuna = 15

print("Operadores aritmeticos")
print("Costo de consulta:", costo_consulta)
print("Costo de vacuna:", costo_vacuna)
print("Total:", costo_consulta + costo_vacuna)
print("Diferencia:", costo_consulta - costo_vacuna)
print("Costo de tres vacunas:", costo_vacuna * 3)
print("Costo compartido entre dos mascotas:", (costo_consulta + costo_vacuna) / 2)
print("Consultas completas que cubre 100:", 100 // costo_consulta)
print("Saldo luego de pagar una consulta con 100:", 100 % costo_consulta)
print("Costo de una vacuna al cuadrado:", costo_vacuna ** 2)

print("Operadores de comparacion")
print("¿La consulta cuesta lo mismo que la vacuna?:", costo_consulta == costo_vacuna)
print("¿La consulta cuesta distinto que la vacuna?:", costo_consulta != costo_vacuna)
print("¿La consulta cuesta mas que la vacuna?:", costo_consulta > costo_vacuna)
print("¿La consulta cuesta al menos 25?:", costo_consulta >= 25)
print("¿La vacuna cuesta menos que la consulta?:", costo_vacuna < costo_consulta)
print("¿La vacuna cuesta como maximo 15?:", costo_vacuna <= 15)

print("Operadores logicos")
mascota_registrada = True
consultorio_abierto = True
print("¿Puede recibir atención?:", mascota_registrada and consultorio_abierto)
print("¿Puede agendar por consulta o vacuna?:", costo_consulta > 0 or costo_vacuna > 0)
print("¿El consultorio está cerrado?:", not consultorio_abierto)