"""
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지
각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
"""

from collections import *
nList = []

for i in range(0, 3):
    nList.append(input())

a, b, c = map(int,nList)
num = a * b * c

num_list = list(str(num))

count_number = Counter(num_list)
for i in range(0,10):
    if count_number['%d'%i] == 0:
        count_number['%d'%i] == 0
    else:
        continue

for i in range(0, 10):
    print(count_number['%d'%i])
