import random
import csv

def generar_rut():
    # Genera un número aleatorio de 7 dígitos
    numero = str(random.randint(1111111, 9999999))

    # Calcula el dígito verificador
    suma = 0
    multiplo = 2
    for i in reversed(numero):
        suma += int(i) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2

    dv = 11 - (suma % 11)
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = 'K'

    # Retorna el RUT completo en formato string
    return f"{numero}-{dv}"

# Crea el archivo CSV y escribe los RUTs generados en él
with open('DNI.csv', mode='w', newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    ruts_generados = set()  # Para mantener un conjunto de RUTs generados

    # Escribe los RUTs generados en el archivo CSV
    for i in range(1000):
        rut = generar_rut()
        escritor_csv.writerow([rut])
        ruts_generados.add(rut)

print("La generación de RUTs ha finalizado.")
