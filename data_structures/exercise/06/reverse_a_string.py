text_to_reverse = "Hi My name is Andrei"


def reverse(string):
    result = []
    for char in string:
        result.append(char)
    result.reverse()
    return "".join(result)


print(text_to_reverse)
print(reverse(text_to_reverse))


def reverse2(string):
    result = ""
    end =( len(string) + 1) * (-1) 
    for i in range(-1, end, -1):
        result += string[i]
    return result


print(reverse2(text_to_reverse))