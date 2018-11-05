# -*- coding: utf-8 -*-

import datetime

def sum1toN(n) :  #함수 선언
    sum = 0       # 값 초기화
    for a in range(n+1) :  #a가 0부터 시작하므로 n+1까지를 범위로 지정
        sum += a  # sum = sum + a
    return sum

def sum1toNSecond(n) :
    sum = 0
    sum = n *(n+1) / 2
    return sum

startTime = datetime.datetime.now()
print('sum = %d' % sum1toN(10000000))
endTime = datetime.datetime.now()
print("sum1toN", endTime - startTime)

startTime = datetime.datetime.now()
print('sum = %d' % sum1toNSecond(10000000))
endTime = datetime.datetime.now()
print("sum1toNSecond", endTime - startTime)