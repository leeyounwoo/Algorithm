import sys
sys.stdin = open('input.txt')

def translator(num): # 후위 표기식 변환기
    stack = [] # 연산자 전용
    result = [] # 리턴값 만들기

    for i in num:
        if i.isdigit():  # 숫자는 result에
            result.append(i)

        elif i == '*':  # 연산자는 stack에
            stack.append(i)

        elif i == '+':  # 더하기
            if len(stack) > 0:
                while stack:  # stack에 있는걸 역순으로 다 넣어줘야함
                    popped = stack.pop()
                    result.append(popped)
                stack.append(i)
            else:
                stack.append(i)

    while stack: # 나머지 연산자들 result 뒤에 넣기
         result.append(stack.pop())

    return result

def caculator(s): # 후위 표기식 계산기
    stack = []

    for i in s:
        if i.isdigit():
            stack.append(int(i))

        elif i == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)

        elif i == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)

    answer = stack.pop()
    return answer

for tc in range(1, 11):
    n = int(input())
    num = input()

    num = translator(num) # 후위 표기식 변환
    answer = caculator(num) # 후위 표기식 계산
    print('#{} {}'.format(tc, answer))


