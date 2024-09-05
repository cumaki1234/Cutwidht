import random
from typing import List

def generar_permutaciones(arr: List[int]) -> List[List[int]]:
    resultado = []

    def permutar(actual: List[int], resto: List[int]):
        if len(resto) == 0:
            resultado.append(actual)
            return

        for i in range(len(resto)):
            nuevo_actual = actual + [resto[i]]
            nuevo_resto = resto[:i] + resto[i + 1:]
            permutar(nuevo_actual, nuevo_resto)

    permutar([], arr)
    return resultado

def generar_vector(n: int) -> List[int]:
    return list(range(1, n + 1))

def generar_vector_aleatorio(n: int) -> List[int]:
    vector = list(range(1, n + 1))
    for i in range(len(vector) - 1, 0, -1):
        j = random.randint(0, i)
        vector[i], vector[j] = vector[j], vector[i]
    return vector
