# quickSort.py

# Função Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Se a lista tiver um ou zero elementos, já está ordenada
    else:
        pivot = arr[len(arr) // 2]  # Escolhe o pivô como o elemento central
        left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
        middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
        right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
        return quick_sort(left) + middle + quick_sort(right)  # Recursão nas sublistas
