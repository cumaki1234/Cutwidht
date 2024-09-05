import sys
import os
import time

# Agregar la ruta de la carpeta raíz del proyecto al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import TratamientoData
import Permutaciones
import CudWidth

# Variables globales
Numero_Muestras = 100
Numero_Poblacion = 3

def main():
    start_time = time.time()  # Iniciar el temporizador

    Data = TratamientoData.TratamientoData.leer_archivo()

    if Data.strip() == "":
        print("Archivo Fuente Vacío")
        return

    print("El archivo no está vacío y se procede al tratamiento de los datos")
    Encabezado = TratamientoData.TratamientoData.crear_encabezado(Data)
    print("Encabezado")
    print(Encabezado)
    NombreArchivo = TratamientoData.TratamientoData.obtener_fecha_hora_actual()
    TratamientoData.TratamientoData.escribir_archivo("Encabezado", NombreArchivo)
    TratamientoData.TratamientoData.escribir_archivo(Encabezado, NombreArchivo)

    Matriz = TratamientoData.TratamientoData.crear_matriz_filas(Data)

    if Encabezado[0] != Encabezado[1]:
        print("El número de vértices no coincide")
        return

    if Encabezado[2] == 0:
        print("El número de aristas es 0")
        return

    if Encabezado[2] != len(Matriz):
        print(f"El número de aristas {Encabezado[2]} es diferente del número de adyacencias de la matriz {len(Matriz)}")
        return

    Maximo = 0
    Minimo = 0
    Min_Cud = 0
    Min_Muestra = 0

    for i in range(1, Numero_Muestras + 1):
        TratamientoData.TratamientoData.escribir_archivo("-----------------------------------------------------------------------------------------------", NombreArchivo)
        TratamientoData.TratamientoData.escribir_archivo(f"Muestra: {i}", NombreArchivo)

        print(f"Muestra número: {i}")
        Maximo = 0
        Minimo = 0

        for j in range(1, Numero_Poblacion + 1):
            TratamientoData.TratamientoData.escribir_archivo(".....................................", NombreArchivo)
            print(f"Población: {j}")

            VectorCombinacion = Permutaciones.generar_vector_aleatorio(Encabezado[0])
            print(VectorCombinacion)
            TratamientoData.TratamientoData.escribir_archivo(f"Población {j}  : [ {VectorCombinacion} ]", NombreArchivo)

            CudWidthCaculado = CudWidth.calcular_cutwidth(VectorCombinacion, Matriz, NombreArchivo)
            print(f"Máximo CUdWidth calculado de la combinación: {CudWidthCaculado}")
            TratamientoData.TratamientoData.escribir_archivo(f"Máximo CUdWidth calculado de la combinación: {CudWidthCaculado}", NombreArchivo)

            if Minimo == 0:
                Minimo = CudWidthCaculado
            if CudWidthCaculado < Minimo:
                Minimo = CudWidthCaculado

        TratamientoData.TratamientoData.escribir_archivo("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -", NombreArchivo)
        TratamientoData.TratamientoData.escribir_archivo(f"Mínimo encontrado en la muestra número: {i} es de: W={Minimo}", NombreArchivo)

        if Min_Cud == 0:
            Min_Cud = Minimo
        if Minimo < Min_Cud:
            Min_Cud = Minimo
            Min_Muestra = i

    TratamientoData.TratamientoData.escribir_archivo("    ", NombreArchivo)
    TratamientoData.TratamientoData.escribir_archivo("    ", NombreArchivo)
    TratamientoData.TratamientoData.escribir_archivo("//////--------------[ R E S U L T A D O ]--------------\\\\\\", NombreArchivo)
    TratamientoData.TratamientoData.escribir_archivo(f"Mínimo CudWidht encontrado es de : W={Min_Cud} de la muestra número: {Min_Muestra}", NombreArchivo)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución total: {execution_time} segundos")
    TratamientoData.TratamientoData.escribir_archivo(f"Tiempo de ejecución total: {execution_time} segundos", NombreArchivo)

if __name__ == "__main__":
    main()
