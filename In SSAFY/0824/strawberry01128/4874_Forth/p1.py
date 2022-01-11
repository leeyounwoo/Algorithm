import sys
sys.stdin = open('input.txt')
def forth(text):
    stack = []
    answer = 0
    for i in text:
        # . 빼고 연산 친구들을 만난다면?
        if (i == '+' or i == '-'
                or i == '*' or i == '/'):
            # 연산 친구들이 왔는데 숫자 친구가 2명이 있다면?
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    answer = int(a) + int(b)
                    stack.append(answer)
                elif i == '-':
                    answer = int(a) - int(b)
                    stack.append(answer)
                elif i == '*':
                    answer = int(a) * int(b)
                    stack.append(answer)
                elif i == '/':
                    answer = int(a) // int(b)
                    stack.append(answer)
            else:
                return 'error'

        # 대장 . 친구가 왔다.
        elif i == '.':
            if len(stack) == 1:
                return answer
            else:
                return 'error'

        else:
            stack.append(i)

T = int(input())
for tc in range(1,T+1):
    text = list(map(str, input().split()))
    print('#{} {}'.format(tc,forth(text)))


'''
# 중위표기법 => 후위표기법 변환 문제
string = '2+3*4/5'
stack = []

# 수식을 읽는 부분
for i in range(len(string)):
    char = string[i]
    if (char == '+' or char == '-'
            or char == '*' or char == '/'):
        stack.append(char)
    else:
        print(char, end="")

# stack에 남아있는 부분 pop
while stack:
    print(stack.pop(), end="")


import sys
sys.stdin = open('input.txt')
'''