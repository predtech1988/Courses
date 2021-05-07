#Bruteforce method (array is sorted)

array1 = [1, 2, 3, 9]
array2 = [1, 2, 4, 4]
array3 = [6,4,3,2,1,7]
summ = 8


def find_pair_v1(arr, summ):
    arr_length = len(arr)
    for i in range(arr_length):
        j = i +1
        #Cheking for "Index out of range" and if sum of the pair = sum"
        if (j < arr_length) and (arr[i] + arr[j] == summ):
            return True


#Bruteforce method (array not sorted)
def find_pair_v2(arr, summ):
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(1, arr_length):
            #print(arr[i]+ arr[j])
            if arr[i]+ arr[j] == summ:
                return True            
    return False


#Using Set to solve (array not sorted)
def find_pair_v3(arr, summ):
    complement = set()
    for value in arr:
        if (value in complement):
            return True
        complement.add(summ - value)
    return False


print(find_pair_v1(array2, summ))
print(find_pair_v2(array3, 9))
print(find_pair_v3(array2, 2))
