import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    string = input()

    # 후위 표기식으로 바꾸기
    stack = []
    result = []

    for s in string:
        if s == '+':
            while stack:
                result.append(stack.pop())
            stack.append(s)
        elif s == '*':
            stack.append(s)
        else:
            result.append(s)

    while stack:
        result.append(stack.pop())

    # 변환된 식 계산하기
    for x in result:
        if x == '+':
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1 + num2)
        elif x == '*':
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1 * num2)
        else:
            stack.append(x)

    print('#{} {}'.format(t, stack.pop()))