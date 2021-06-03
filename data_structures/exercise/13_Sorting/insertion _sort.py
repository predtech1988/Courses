# Made with help of the https://youtu.be/yCxV0kBpA6M
# Need more practice, re implementate in mid's of june 2021
# arr_list = [5, 4, 10, 1, 6, 2]
arr_list = [1, 2, 3, 4, 5]


def insertion_sort(arr):
    arr_len = len(arr)
    for i in range(1, arr_len):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp


insertion_sort(arr_list)
