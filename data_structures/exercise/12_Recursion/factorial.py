def factorial_recursive(number):
    if number == 2:
        return 2
    return number * factorial_recursive(number - 1)


def factorial_iterative(number):
    summ = 1

    while number > 1:
        summ *= number
        number -= 1
    print(summ)


factorial_iterative(10)
print(factorial_recursive(5))
