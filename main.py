from dados import lanzar_dados

def main():
    num_dados = int(input("Introduce el número de dados a lanzar: "))
    resultados = lanzar_dados(num_dados)
    print(f"Resultados: {resultados}")

if __name__ == "__main__":
    main()
