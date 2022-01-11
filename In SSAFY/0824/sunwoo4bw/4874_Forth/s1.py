import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    input_lst = input().split()
    stack = []
    fail = 0
    try:
        for i in input_lst:
            # True 숫자 - stack에 추가
            if i.isdigit():
                stack.append(int(i))
            # False
            elif i == '+':
                b, a = s
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                stack.append(stack.pop() - stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                stack.append(stack.pop() // stack.pop()) # 나누어 떨어진대
            else:
                answer = stack.pop() # 84
                if not len(stack) == 0: # '.' -> stack에 숫자 있으면 실패
                    fail = 1
                break
    # 숫자-연산자 짝이 안맞아?
    except:
        fail = 1
    if fail:
        print('#{}'.format(tc), end=' ')
        print('error')
    else:
        print('#{} {}'.format(tc, answer))




    # 숫자를 stack에 넣어라
    # for i in range(len(input_lst)):
    #     char = input_lst[i]
    #     if (char != '+' and char != '-' and char != '*' and char != '/' and char != '.'):
    #         stack.append(char)

    # for i in range(len(input_lst)-1):
    #     if input_lst[i].isdigit():
    #         stack.append(input_lst[i])
