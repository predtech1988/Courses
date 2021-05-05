# // Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# //For Example:
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# //should return false.
# //-----------
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# //should return true.

# // 2 parameters - arrays - no size limit
# // return true or false

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']


#Nested for loop's
def is_contains_common_item_brutforce(arr1, arr2):
    for elem1 in arr1:
        for elem2 in arr2:
            if elem1 == elem2:
                return True
    return False


#Dictionary (hashtable)
def is_contains_common_item(arr1, arr2):
    table = {item: True for item in arr1}
    for item in arr2:
        if(table.get(item)):
            return True
    return False


#Nested loop's with sugar
def is_contains_common_item_2(arr1, arr2):
    for item in arr1:
        if item in arr2:
            return True
    return False


print(is_contains_common_item_brutforce(array1, array2))
print(is_contains_common_item(array1, array2))
print(is_contains_common_item_2(array1, array2))
