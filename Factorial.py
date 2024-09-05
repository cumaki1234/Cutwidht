class Factorial:

    @staticmethod
    def calcular(numero):
        # Verificar si el número es negativo, cero o uno
        if numero < 0:
            return "No existe factorial para números negativos"
        elif numero == 0 or numero == 1:
            return 1
        else:
            # Calcular el factorial
            resultado = 1
            for i in range(2, numero + 1):
                resultado *= i
            return resultado

# Uso del objeto Factorial
factorial = Factorial()

# Ejemplo de cómo invocar la función calcular
numero = 5
resultado = factorial.calcular(numero)
print(f"El factorial de {numero} es: {resultado}")
