import random
import time
import sys

sys.setrecursionlimit(1000000)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menores = [x for x in arr[1:] if x <= pivot]
    mayores = [x for x in arr[1:] if x > pivot]
    return quick_sort(menores) + [pivot] + quick_sort(mayores)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])
        result = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        result += L[i:]
        result += R[j:]
        return result
    else:
        return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

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



def ejecutar_pruebas(nombre_algoritmo, algoritmo):
    print(f"\n🧪 Pruebas para {nombre_algoritmo} (máximo 12,000 elementos)\n")
    tamaños = {
        "Small (2,000)": 2000,
        "Medium (6,000)": 6000,
        "Large (12,000)": 12000,
    }
    for nombre, tamaño in tamaños.items():
        print(f"--- {nombre} ---")
        try:
            medir_tiempos(algoritmo, tamaño)
        except RecursionError:
            print(" Error de recursión: el tamaño es muy grande para este algoritmo.\n")



if __name__ == "__main__":
    ejecutar_pruebas("Heap Sort", heap_sort)
    ejecutar_pruebas("Quick Sort", quick_sort)
    ejecutar_pruebas("Merge Sort", merge_sort)
    ejecutar_pruebas("Selection Sort", selection_sort)
    ejecutar_pruebas("Bubble Sort", bubble_sort)
    ejecutar_pruebas("Insertion Sort", insertion_sort)

