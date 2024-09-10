# mergeSort.py

# Função Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Divide a lista ao meio
        left_half = arr[:mid]  # Metade esquerda
        right_half = arr[mid:]  # Metade direita

        # Recursão nas metades
        merge_sort(left_half)
        merge_sort(right_half)

        # Variáveis para as sublistas
        i = j = k = 0

        # Intercala as sublistas esquerda e direita
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se sobrou algo na sublista esquerda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verifica se sobrou algo na sublista direita
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr
