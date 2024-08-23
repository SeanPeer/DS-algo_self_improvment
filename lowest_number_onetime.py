def lowest(arr):
    current_low = arr[0]

    for i in range(len(arr)):
        if arr[i] < current_low:
            current_low = arr[i]

    return current_low


