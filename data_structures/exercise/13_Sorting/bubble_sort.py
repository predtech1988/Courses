array = [88, 2, 65, 34, 2, 1, 7, 8]
array_2 = [88, 2, 65, 34, 2, 1, 7, 8]


def bubble(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(i + 1, arr_len):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


def bubble_v2(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


bubble(array)
# bubble_v2(array_2)
print(array)
