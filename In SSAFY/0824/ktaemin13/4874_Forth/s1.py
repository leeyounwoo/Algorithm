import sys
sys.stdin = open('input.txt')


# 예상되는 오류: stack에 숫자만 있을 때! => 정답..
def forth():
    stack = []
    operation = ['+', '-', '*', '/']
    for i in range(len(arr)):
        if arr[i] in operation and len(stack) < 2:  # 연산자인데, stack이 비어있거나 숫자 1개가 있을 경우
            return 'error'
        if arr[i] == '.' and stack:  # . 이 나왔는데 stack이 비어있지 않다면!
            return 'error'
        if arr[i] == '+':
            if arr[i+1] in operation and len(stack) < 2:  # 다음 값이 연산자이고, stack이 비어있거나 숫자 1개가 있을 경우
                return 'error'
            stack.append(int(stack[-1]) + int(stack[-2]))  # stack에 연산하고 그 값을 추가
            if arr[i + 1] == '.' and len(stack) == 3:      # 그 후 다음 값이 마침표이고 stack에 숫자가 3개라면
                return stack[-1]                           # 출력
            else:                                          # 뒤에서부터 연산 결괏값 다음번째인 -2번째를 2번 pop함
                stack.pop(-2)
                stack.pop(-2)
        elif arr[i] == '-':
            if arr[i+1] in operation and len(stack) < 2:
                return 'error'
            stack.append(int(stack[-2]) - int(stack[-1]))
            if arr[i + 1] == '.' and len(stack) == 3:
                return stack[-1]
            else:
                stack.pop(-2)
                stack.pop(-2)
        elif arr[i] == '*':
            if arr[i+1] in operation and len(stack) < 2:
                return 'error'
            stack.append(int(stack[-1]) * int(stack[-2]))
            if arr[i + 1] == '.' and len(stack) == 3:
                return stack[-1]
            else:
                stack.pop(-2)
                stack.pop(-2)
        elif arr[i] == '/':
            if arr[i+1] in operation and len(stack) < 2:
                return 'error'
            stack.append(int(stack[-2]) // int(stack[-1]))
            if arr[i + 1] == '.' and len(stack) == 3:
                return stack[-1]
            else:
                stack.pop(-2)
                stack.pop(-2)
        else:  # 숫자라면 append
            stack.append(arr[i])


T = int(input())

for tc in range(T):
    arr = list(map(str, input().split()))

    print('#{} {}'.format(tc+1, forth()))
