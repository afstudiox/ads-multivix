# desempenho.py
import timeit
from lista import gerar_lista  # importa a função gerar_lista do arquivo lista.py
from bubbleSort import bubble_sort  # importa a função bubble_sort do arquivo bubbleSort.py
from insertionSort import insertion_sort  # importa a função insertion_sort do arquivo insertionSort.py
from mergeSort import merge_sort  # importa a função merge_sort do arquivo mergeSort.py
from quickSort import quick_sort  # importa a função quick_sort do arquivo quickSort.py

# Wrapper que passa a lista para o Bubble Sort
def wrapper_bubble_sort(lista):    
    bubble_sort(lista)

# Wrapper que passa a lista para o Insertion Sort
def wrapper_insertion_sort(lista):
    insertion_sort(lista)

# Wrapper que passa a lista para o Merge Sort
def wrapper_merge_sort(lista):
    merge_sort(lista)

# Wrapper que passa a lista para o Quick Sort
def wrapper_quick_sort(lista):
    quick_sort(lista)

# Gerar lista de 1000 números aleatórios entre 1 e 1000
lista = gerar_lista()

# Medir o tempo de execução de 1000 execuções com Bubble Sort
execution_time_bubble = timeit.timeit(lambda: wrapper_bubble_sort(lista.copy()), number=1000)
print(f"Execution time (Bubble Sort): {execution_time_bubble:.6f} segundos para 1000 execuções")

# Medir o tempo de execução de 1000 execuções com Insertion Sort
execution_time_insertion = timeit.timeit(lambda: wrapper_insertion_sort(lista.copy()), number=1000)
print(f"Execution time (Insertion Sort): {execution_time_insertion:.6f} segundos para 1000 execuções")

# Medir o tempo de execução de 1000 execuções com Merge Sort
execution_time_merge = timeit.timeit(lambda: wrapper_merge_sort(lista.copy()), number=1000)
print(f"Execution time (Merge Sort): {execution_time_merge:.6f} segundos para 1000 execuções")

# Medir o tempo de execução de 1000 execuções com Quick Sort
execution_time_quick = timeit.timeit(lambda: wrapper_quick_sort(lista.copy()), number=1000)
print(f"Execution time (Quick Sort): {execution_time_quick:.6f} segundos para 1000 execuções")

# Armazenar o resultado da lista ordenada usando Bubble Sort
# lista_ordenada_bubble = bubble_sort(lista.copy())
# print("Lista ordenada com Bubble Sort:", lista_ordenada_bubble)

# Armazenar o resultado da lista ordenada usando Insertion Sort
# lista_ordenada_insertion = insertion_sort(lista.copy())
# print("Lista ordenada com Insertion Sort:", lista_ordenada_insertion)

# Armazenar o resultado da lista ordenada usando Merge Sort
# lista_ordenada_merge = merge_sort(lista.copy())
# print("Lista ordenada com Merge Sort:", lista_ordenada_merge)

# Armazenar o resultado da lista ordenada usando Quick Sort
# lista_ordenada_quick = quick_sort(lista.copy())
# print("Lista ordenada com Quick Sort:", lista_ordenada_quick)
