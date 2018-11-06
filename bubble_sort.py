a = [1, 4,5,6,2,3,687,9 ,3,1,23,25, 234234, 111,0, -1, -2]

def bubble_sort(list) :
    temp = 0
    for i in range(len(list)) :
        for j in range(i+1, len(list)) :
            if list[i] > list[j] :
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

'''파이썬에서는
파이썬에서는 다음과 같이 한 줄로 두 값을 바꿔치기할 수 있습니다.

a = 3
b = 'abc'

a, b = b, a # 참 쉽죠?
'''

def bubble_sortPy(list) :
    for i in range(len(list)) :
        for j in range(i+1, len(list)) :
            if list[i] > list[j] :
                list[i], list[j] = list[j], list[i]
    return list

def bubble_sortMin(list) :
    for i in range(len(list)) :
        for j in range(i+1, len(list)) :
            if list[i] < list[j] :
                list[i], list[j] = list[j], list[i]
    return list
print(bubble_sort(a))
print(bubble_sortPy(a))
print(bubble_sortMin(a))