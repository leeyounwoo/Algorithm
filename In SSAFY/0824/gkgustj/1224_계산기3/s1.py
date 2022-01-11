import sys
sys.stdin = open('input.txt')

def change_after(string):
    # 스택 안에 있을 때 우선순위
    isp = {'(': 0, '+': 1, '-': 1,
           '*': 2, '/': 2}
    # 스택 밖에 있을 때 우선순위
    icp = {'(': 3, '+': 1, '-': 1,
           '*': 2, '/': 2}

    stack = []
    result = []

    i = 0
    while i < len(string):
        # 문자가 숫자라면 result에 추가
        if string[i].isnumeric():
            result.append(string[i])
        else:
            # 스택이 비었다면 연산자를 스택에 추가
            if not stack:
                stack.append(string[i])

            # 연산자가 )라면, (가 나올 때까지 스택의 top을 빼서 result에 추가
            elif string[i] == ')':
                while stack[-1] != '(':
                    result.append(stack.pop())
                # 스택에 있는 ( 빼기
                stack.pop()

            # 스택의 top보다 우선순위가 낮은 연산자라면,
            # 우선순위가 높은 연산자를 만날 때까지 스택에서 top을 빼서 result에 추가
            elif icp[string[i]] <= isp[stack[-1]]:
                while stack and icp[string[i]] <= isp[stack[-1]]:
                    result.append(stack.pop())
                stack.append(string[i])

            # 스택의 top보다 우선순위가 높은 연산자라면, 스택에 추가
            elif icp[string[i]] > isp[stack[-1]]:
                stack.append(string[i])

        i += 1

    # 만약 스택에 남은 연산자가 있다면 모두 result에 추가
    if stack:
        result.append(stack.pop())

    return result


def calculation(string):
    stack = []

    for s in string:
        # 문자가 만약 숫자이면 정수형으로 바꿔서 스택에 push
        if s.isnumeric():
            stack.append(int(s))

        # 연산자라면, 스택에서 2개의 숫자를 pop해서 연산한 후 다시 스택에 push
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if s == '+':
                stack.append(num2+num1)
            elif s == '-':
                stack.append(num2-num1)
            elif s == '*':
                stack.append(num2*num1)
            elif s == '/':
                stack.append(num2//num1)

    return stack.pop()


for t in range(1, 11):
    N = int(input())
    string = input()

    new_string = change_after(string)

    print('#{} {}'.format(t, calculation(new_string)))