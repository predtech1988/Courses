boxes = [1, 2, 3, 4, 5]

def log_all(array):
    array_length = len(array)
    for box in array:
        for i in range(array_length):
            print(box, array[i])


log_all(boxes)