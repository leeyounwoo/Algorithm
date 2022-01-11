import sys
sys.stdin = open('input.txt')

# CAAABBA
# CABBA
# CAA
# C -> return 1
# 글자가 3번이상 연속되도 2개짜리만 지운다!

def check(s):
    stack = []
    for i in s:
        if len(stack) == 0: # index 에러를 막기 위해
            stack.append(i)

        elif stack[-1] == i: # stack이 비어있을때 인덱싱에러 날까봐
            stack.pop()

        else:
            stack.append(i)

    return len(stack)

t = int(input())

for tc in range(1, t+1):
    s = input()

    print('#{} {}'.format(tc, check(s)))