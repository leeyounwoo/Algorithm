import sys
sys.stdin = open('0924/woosteelz/1232_사칙연산/input.txt')

operator = ['+', '-', '/', '*']


def cal(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '/':
        return a / b
    elif operator == '*':
        return a * b


for tc in range(10):
    n = int(input())
    tree = ['' for _ in range(n+1)]

    for _ in range(n):
        temp = list(map(str, input().split()))
        if temp[1].isdigit():
            tree[int(temp[0])] = [int(temp[1])]
        else:
            tree[int(temp[0])] = [temp[1], int(temp[2]), int(temp[3])]
    for num in range(n, 0, -1):
        if tree[num][0] in operator:
            tree[num] = [cal(tree[num][0], tree[tree[num][1]][0],
                             tree[tree[num][2]][0])]

    print(f'#{tc+1} {int(tree[1][0])}')
