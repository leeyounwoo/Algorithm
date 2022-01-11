import sys
sys.stdin = open('input.txt')


def calculator():
    stack = []
    cal = ''
    for i in arr:
        if i == '*':
            stack.append(i)
        elif i == '+':
            while stack:
                cal += stack.pop()
            stack.append(i)
        else:
            cal += i
    while stack:
        cal += stack.pop()

    result = []
    for i in cal:
        if i == '*':
            num_2 = result.pop()
            num_1 = result.pop()
            result.append(num_2 * num_1)
        elif i == '+':
            num_2 = result.pop()
            num_1 = result.pop()
            result.append(num_2 + num_1)

        else:
            result.append(int(i))

    return result[0]


for tc in range(1):
    n = int(input())
    arr = list(map(str, input()))
    print('#{} {}'.format(tc+1, calculator()))
