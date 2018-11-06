def factorial(n) :
    result = 1
    for i in range(1, n + 1) :
        result *= i
    return result

print(factorial(5))

def recursive_factorial(n) :
    if n == 1 :
        return 1
    return n * recursive_factorial(n - 1)

print(recursive_factorial(5))
