def insertion_sort(arr):
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(arr)):
        # O elemento atual a ser inserido na sublista ordenada
        key = arr[i]
        # Index do elemento anterior ao atual
        j = i - 1
        
        # Move os elementos da sublista ordenada que são maiores que a 'key'
        # para a direita, até encontrar a posição correta
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Desloca o elemento
            j -= 1
        
        # Insere a 'key' na posição correta
        arr[j + 1] = key
    
    return arr