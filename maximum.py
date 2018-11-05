v = [17, 3, 1, 10, 2, 23, 34, 10792, 18, 33, 58, 7, 33, 42, 100, 101]

def findMax(list):
    max = list[0]
    for a in range(len(list)):
        if max < list[a] :
            max = list[a]
    return max

def findMaxIndex(list):
    max = list[0]
    i = 0
    for a in range(len(list)):
        if max < list[a] :
            max = list[a]
            i = a
    return i

print(findMax(v))
print(findMaxIndex(v))

i, j, k, l = map(int, input('숫자 4개를 입력해주세요 ').split())

a = [i, j, k, l]

def find_min(list):
    min = list[0]
    for a in range(len(list)):
        if min > list[a] :
            min = list[a]
    return min

print(find_min(a))