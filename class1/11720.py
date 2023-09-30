"""
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
"""

import sys

num_len = int(sys.stdin.readline())
sum = 0

num = list(sys.stdin.readline().rstrip())

for i in range(0, num_len):
    sum += int(num[i])

print(sum)
