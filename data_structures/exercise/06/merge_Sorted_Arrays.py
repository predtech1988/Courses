#Naive version
def merge_sorted(arr1, arr2):
    #check input
    #create empty list
    answer = []
    #read array's one by one, and add items to "empty list"
    for item in arr1:
        answer.append(item)
    
    for item in arr2:
        answer.append(item)
    #at the end use .sort() methon on "empty list"
    answer.sort()
    return answer


#Naive version with python power :))  (built in methods)  extend() .sort()
def merge_sorted_2(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    return arr1

def merge_sorted_3(arr1, arr2):
    """
    Ugly but working. Not scalebel at all. Need more work.
    When i receive 2 array's, 
    i determinate the size of it, and place bigger or
    equal to the "bigger", than i use "i_end" to save
    length of array, and choose smaller to iterate.  
    When reached end of smaller, assuming that array
    is sorted, i just copy left items from the bigger.
    """
    answer = []
    i = 0
    j = 0

    if len(arr1) >= len(arr2):  #i bigger list
        i_end = len(arr1)
        j_end = len(arr2)
        bigger = arr1
        smaller = arr2
    else:
        i_end = len(arr2)
        j_end = len(arr1)
        bigger = arr2
        smaller = arr1

    for step in range((i_end + j_end)-1):
        a = bigger[i]
        if j < j_end: #Until we reach end of the smaller list            
            b = smaller[j]
            if a < b:
                answer.append(a)
                i +=1
            elif a > b:
                answer.append(b)
                j +=1                
            else:
                answer.append(a)
                answer.append(b)
                j +=1
                i +=1
        else:            
            answer.append(a)
            i +=1
    print(answer)

print(merge_sorted([0,3,4,31], [4,6,30]))
print(merge_sorted_2([0,3,4,31], [4,6,30]))
merge_sorted_3([0,3,4,31], [4,6,30])
merge_sorted_3([4,6,30], [0,3,4,31])

