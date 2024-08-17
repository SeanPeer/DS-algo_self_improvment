def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


def fib_dp(n):
    helper = {0: 0,
              1: 1}

    def f(n):
        if n in helper:
            return helper[n]
        else:
            helper[n] = f(n - 1) + f(n - 2)
            return helper[n]

    return f(n)


print(fib_dp(10))
