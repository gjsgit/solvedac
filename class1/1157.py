'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
'''

# from collections import *, list(), .upper()
from collections import *
ch = list(input().upper())
ch_count = Counter(ch)
most = ch_count.most_common()
if len(most) == 1:
    print(list(most[0])[0])
else:
    if list(most[0])[1] == list(most[1])[1]:
        print("?")
    else:
        print(list(most[0])[0])
