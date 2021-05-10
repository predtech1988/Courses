#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Bonus... What if we had this:
# [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2

#Bad version with nested loops, code not readable 
#Remove print()
def firstRecurringCharacter(arr):
    id_map = {}
    already_seen = set()
    arr_len = len(arr)    
    #Searching for position's of the pair 
    for i in range(arr_len):
        for j in range(i+1,arr_len):
            if   (arr[i] not in already_seen) and (arr[i] == arr[j]):
                already_seen.add(arr[i])
                id_map[(arr[i])] = (j - i)
                break
    #Need to redo this part. Searching for the smaller difference in the pair. 
    minimum_difference = [None, None]     #1st element difference 2nd key for dictionary
    for key in id_map:
        if minimum_difference[0] == None:
            minimum_difference[0] = id_map[key]
            minimum_difference[1] = key
        if (minimum_difference[0] >= id_map[key]):
            minimum_difference[0] = id_map[key]
            minimum_difference[1] = key
    if minimum_difference[1] == None:
        return print("None")
    return print(minimum_difference[1])


firstRecurringCharacter([2,5,1,2,3,5,1,2,4])    #Answer 2
firstRecurringCharacter([2,1,1,2,3,5,1,2,4])    #Answer 1
firstRecurringCharacter([2,3,4,5])              #Answer None
firstRecurringCharacter([2,5,5,2,3,5,1,2,4])    #Answer 5
firstRecurringCharacter([2])                    #Answer None
