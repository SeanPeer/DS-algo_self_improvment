def quick_sort(arr, low, high):
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        # Recursively sort elements before and after the partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def swap(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp


def partition(arr, low, high):
    # Choose the last element as the pivot
    pivot = arr[high]
    i = low - 1  # Pointer for the greater element

    # Traverse through all elements and compare each with the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If the element is smaller than or equal to the pivot
            i += 1  # Increment the greater element pointer
            swap(arr, i, j)  # Swap elements at i and j

    # Swap the pivot element with the element at i+1
    swap(arr, i + 1, high)
    return i + 1  # Return the pivot index


# Example usage:
array = [5, 7, 8, 6, 3, 12, 5, 8, 1]
quick_sort(array, 0, len(array) - 1)
print("Sorted array:", array)
