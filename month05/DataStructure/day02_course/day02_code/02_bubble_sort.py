def bubble_sort(array):
    arr_len = len(array)
    if arr_len == 1:
        return array
    for i in range(arr_len - 1):
        for j in range(arr_len - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


list01 = [324, 4, 32, 4, 5325, 234, 5, 4, 23]
list02 = [34,4]
bubble_sort(list02)
print(list02)
