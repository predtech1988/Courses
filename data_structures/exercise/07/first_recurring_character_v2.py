#Google Question
#Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2
#Bonus... What if we had this:
# [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2

#New version after watching solution video.
#Remove print()
def firstRecurringCharacter(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]] = i
        else:
            return print(arr[i])
    else:
        return print("None")


firstRecurringCharacter([2,5,1,2,3,5,1,2,4])    #Answer 2
firstRecurringCharacter([2,1,1,2,3,5,1,2,4])    #Answer 1
firstRecurringCharacter([2,3,4,5])              #Answer None
firstRecurringCharacter([2,5,5,2,3,5,1,2,4])    #Answer 5
firstRecurringCharacter([2])                    #Answer None
