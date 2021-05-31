# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
def fib_iterative(n):
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(n - 2):
        summ = a + b
        a = b
        b = summ
        print(summ, end=" ")
    # return summ


def fib_recursion(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


# fib_iterative(3)
print(fib_recursion(5))  # answer=3 -> 0, 1, 1, 2, 3
