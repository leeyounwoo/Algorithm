import sys
sys.stdin = open('input.txt')

def check(s):
    temp = []
    for i in s:
        if i == '(' or i == '{':
            temp.append(i)

        elif i == ')' or i == '}':
            if temp and i == ')' and temp[-1] == '{':
                return 0
            elif temp and i == '}' and temp[-1] == ')':
                return 0
            elif not temp:
                return 0
            else:
                temp.pop()

    if len(temp) == 0:
        return 1
    return 0



t = int(input())

for tc in range(1, t+1):
    s = input()

    print('#{} {}'.format(tc, check(s)))
