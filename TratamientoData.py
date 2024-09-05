import os
from datetime import datetime

class TratamientoData:
    
    @staticmethod
    def leer_archivo() -> str:
        try:
            with open('Fuente.txt', 'r', encoding='utf8') as file:
                data = file.read()
            return data
        except IOError as e:
            print(f"Error al leer el archivo: {e}")
            return ""

    @staticmethod
    def crear_encabezado(contenido: str) -> list:
        # Separar el contenido en líneas
        lineas = contenido.strip().splitlines()

        # Procesar la primera línea
        if lineas:
            # Remover espacios adicionales y separar los números
            numeros = list(map(int, lineas[0].strip().split()))
            return numeros
        return []

    @staticmethod
    def crear_matriz_filas(contenido: str) -> list:
        # Separar el contenido en líneas
        lineas = contenido.strip().splitlines()
        # Inicializar la matriz
        matriz = []
        # Procesar cada línea
        for index, linea in enumerate(lineas):
            # Remover espacios adicionales y separar los números
            numeros = list(map(int, linea.strip().split()))
            if index != 0:
                # Guarda las líneas en una matriz sin el encabezado
                matriz.append(numeros)
        return matriz

    @staticmethod
    def escribir_archivo(texto_enviado, nombre_archivo: str):
        texto = str(texto_enviado) + '\n'  # Agregar un salto de línea al final
        try:
            with open(nombre_archivo, 'a', encoding='utf8') as file:
                file.write(texto)
        except IOError as e:
            print(f"Error al guardar en el archivo: {e}")
            

    @staticmethod
    def obtener_fecha_hora_actual() -> str:
        ahora = datetime.now()

        dia = str(ahora.day).zfill(2)
        mes = str(ahora.month).zfill(2)
        año = str(ahora.year)

        horas = str(ahora.hour).zfill(2)
        minutos = str(ahora.minute).zfill(2)
        segundos = str(ahora.second).zfill(2)

        return f"Resultados/{dia}{mes}{año}{horas}{minutos}{segundos}.txt"
