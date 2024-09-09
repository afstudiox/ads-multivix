import timeit
from lista import gerar_lista # importa a função gerar_lista do arquivo lista.py
from bubbleSort import bubble_sort # importa a função bubble_sort do arquivo bubbleSort.py

# Wrapper que passa a lista
def wrapper(lista):    
    bubble_sort(lista)

# Gerar lista de 100 números aleatórios entre 1 e 1000
lista = gerar_lista()


# Medir o tempo de execução de 1000 execuções
execution_time = timeit.timeit(lambda: wrapper(lista.copy()), number=1000)
print(f"Execution time: {execution_time:.6f} segundos para 1000 execuções")

# Armazenar o resultado da lista ordenada para evitar chamar bubble_sort novamente
lista_ordenada = bubble_sort(lista.copy())

# Exibir a lista ordenada uma vez
print("Lista ordenada:", lista_ordenada)