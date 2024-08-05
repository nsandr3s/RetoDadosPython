import random

def lanzar_dados(num_dados):
    resultados = [random.randint(1, 6) for _ in range(num_dados)]
    return resultados
