import random
import time



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def medir_tiempos(algoritmo, tam):
    resultados = []
    for i in range(5):
        datos = random.sample(range(tam * 10), tam)
        inicio = time.time()
        algoritmo(datos.copy())
        fin = time.time()
        duracion = fin - inicio
        resultados.append(duracion)
        print(f"Prueba {i+1}: {duracion:.6f} segundos")
    promedio = sum(resultados) / len(resultados)
    print(f"Promedio: {promedio:.6f} segundos\n")
    return resultados, promedio

def main():
    print("🧪 Pruebas para Bubble Sort (máximo 12,000 elementos)\n")

    tamaños = {
        "Small (1,000)": 1000,
        "Medium (6,000)": 6000,
        "Large (12,000)": 12000,
    }

    for nombre, tamaño in tamaños.items():
        print(f"--- {nombre} ---")
        medir_tiempos(bubble_sort, tamaño)

if __name__ == "__main__":
    main()
