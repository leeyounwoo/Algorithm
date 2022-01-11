import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    in_str = input()
    num = ''
    stack = []      # + 값 넣어주기
    for i in in_str:
        if i == '+':
            if len(stack) and stack[len(stack) - 1] == '*':
                while True:
                    num += stack.pop()
                    if (not len(stack)) or stack[len(stack) - 1] == '+':
                        break
            stack.append(i)
        elif i == '*':
            stack.append(i)
        else:
            num += i

    while len(stack):
        num += stack.pop()      # 스택에 몰아넣은 +를 num으로 이동

    print(num)

    for j in num:
        if j == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a * b)
        elif j == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        else:
            stack.append(j)
    # print('#{} {}'.format(tc, stack.pop()))