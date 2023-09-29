"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
"""

test_num = int(input())
plus_list = []

for i in range(0, test_num):
    plus_list.append(input().split())
    
for j in range(0, test_num):
    print(int(plus_list[j][0])+int(plus_list[j][1]))
