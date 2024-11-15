import random

def heapify(array, n, i):
    largest = i 
    
    left = 2 * i + 1 
    right = 2 * i + 2  

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i] 

        heapify(array, n, largest)

def HeapSort(array):
    n = len(array) 

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0] 
        heapify(array, i, 0)

def is_array_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
        
    return True

if __name__ == "__main__":
    arr = [random.randint(1, 20) for _ in range(20)] 
    print("Original array:",arr)
    print("Sorted:", is_array_sorted(arr))

    HeapSort(arr) 
    print("\n")
    
    print("Sorted array:",arr)
    print("Sorted:", is_array_sorted(arr))