string_as_arr = ["y", "r", "e", "t", "s", "a", "m", " ", "o", "y", "o", "y"]  #'yoyo mastery'
strring_normal = "yretsam oyoy"
# Right answer is "yoyo mastery"


def reverse_arr_string(word_arr):
    # If string given as array
    flag = True
    i = 0
    j = -1
    cnt = int(len(word_arr) / 2)
    while flag:
        word_arr[i], word_arr[j] = word_arr[j], word_arr[i]
        i += 1
        j -= 1
        if i == cnt:
            flag = False
    answer = ""
    for char in word_arr:
        answer += char
    print(answer)


def reverse_string(string):
    answer = ""
    for i in range(len(string) - 1, -1, -1):
        answer += string[i]
    print(answer)


def reverse_string_v2(string):
    for i in range(len(string) - 1, -1, -1):
        print(string[i], end="")


def str_reverse_recursion(string, length):
    if length == 1:
        return string[0]
    last_letter = string[length - 1]
    all_but_last = str_reverse_recursion(string, length - 1)
    return last_letter + all_but_last


def str_reverse_recursion_v2(string, length):
    if length == 1:
        return string[0]
    last_letter = string[length - 1]
    return last_letter + str_reverse_recursion_v2(string, length - 1)


print(str_reverse_recursion_v2(strring_normal, len(strring_normal)))


# reverse_arr_string(string_as_arr)
# reverse_string(strring_normal)
# reverse_string_v2(strring_normal)

# print(str_reverse_recursion(strring_normal, len(strring_normal)))
# print(delegate(strring_normal, len(strring_normal)))
# print(st_iter(strring_normal, len(strring_normal)))


# IDK is this recursive :( But still working
def reverse_recursive(string, i):
    """
    string - String to reverse
    i - string length -1
    """
    if i == 0:
        print(string[-1], end="")
        return string[-1]
    print(string[i], end="")
    reverse_recursive(string, i - 1)


# reverse_recursive(strring_normal, len(strring_normal) - 1)
