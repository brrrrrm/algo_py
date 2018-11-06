def sum1toN(n) :
    if n == 1 :
        return 1
    return n + sum1toN(n - 1)

print(sum1toN(10))