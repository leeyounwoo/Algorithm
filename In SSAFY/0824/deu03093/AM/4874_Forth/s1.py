import sys
sys.stdin = open('input.txt')

operations = ['+', '-', '*', '/', '.']
def cal(string, N):
    ans = 0
    stack = []
    for i in range(N):
        char = string[i]
        if char in operations:
            if char == '.':
                break
            else:
                # 연산자를 만났는데 피연산자가 2개미만인 경우
                if len(stack) < 2:
                    return 'error'
                else:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    if char == '+':
                        temp = num2 + num1
                    elif char == '-':
                        temp = num2 - num1
                    elif char == '*':
                        temp = num2 * num1
                    elif char == '/':
                        temp = num2 // num1
                    stack.append(temp)
        else:
            stack.append(string[i])

    if len(stack) == 1:
        return stack[0]
    # 모든 연산을 마쳤는데도 피연산자가 남아있는 경우
    else:
        return 'error'

for T in range(1, 1+int(input())):
    string = input().split()
    ans = cal(string, len(string))
    print('#{} {}'.format(T, ans))