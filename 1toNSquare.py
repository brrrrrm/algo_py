def sumSquare(n) :
    sum = 0
    for a in range(n+1) :
        sum += a * a
    return sum

def sumSquareSecond(n) :
    sum = n * (n + 1) * (2 * n + 1) / 6
    return sum

print(sumSquare(10))
print(sumSquareSecond(10))