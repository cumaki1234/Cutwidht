import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TratamientoData
from typing import List, Tuple

def calcular_cutwidth(vector: List[int], adyacencias: List[Tuple[int, int]], nombre_archivo: str) -> int:
    n = len(vector)
    max_cutwidth = 0

    # Crear un diccionario de índices para el vector
    indices = {val: idx for idx, val in enumerate(vector)}

    # Cortes en posición en el vector
    for i in range(n - 1):
        cutwidth = 0

        # Número de aristas que cruzan el corte en la posición i
        for u, v in adyacencias:
            pos_u = indices[u]
            pos_v = indices[v]
            if (pos_u <= i and pos_v > i) or (pos_v <= i and pos_u > i):
                cutwidth += 1

        print(f"Cutwidth Calculado: {cutwidth}")
        TratamientoData.TratamientoData.escribir_archivo(f"Cutwidth Calculado: {cutwidth} en el corte: {i+1}", nombre_archivo)

        # Máximo cutwidth encontrado
        if cutwidth > max_cutwidth:
            max_cutwidth = cutwidth

    return max_cutwidth
