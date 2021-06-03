array = [88, 2, 65, 34, 2, 1, 7, 8]


def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        flag = False
        minn = arr[i]
        maxx = minn
        for j in range(i + 1, arr_len):
            if arr[j] < minn:
                minn = arr[j]
                maxx = j  # index to insert maximum number
                flag = True
        if flag:
            arr[maxx] = arr[i]
            arr[i] = minn


selection_sort(array)
print(array)
