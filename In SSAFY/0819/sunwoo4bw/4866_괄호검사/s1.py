import sys
sys.stdin = open('input.txt')
# 여는 괄호 - 스택에 push
# 닫는 괄호 - 스택에 있는 여는 괄호 pop
# 스택에 아무것도 없을 때 끝
# 정상적인 괄호면 1, 아니면 0

T = int(input())
for tc in range(1, T + 1) :
    stack = []

    result = 1
    bracket = input()
    for i in range(0, len(bracket)): # 길이만큼 반복
        if bracket[i] == '(' or bracket[i] == '{':     # open -> append to stack
            stack.append(bracket[i])
        elif bracket[i] == ')' or bracket[i] == '}' :  # close
            if len(stack) == 0: # stack이 비어있으면, 이미 틀렸어
                result = 0
                break
            elif (bracket[i] == ')' and stack.pop()  != '(') or (bracket[i] == '}' and stack.pop()  != '{') :
            # bracket이 } 이고 stack의 마지막에 있는 애가 { 아니면 (즉, {} 성립X)
                result = 0
                break

    if len(stack) == 0:
        result = 1
    else :
        result = 0
    #
    # if stack :
    #     result = 0


    print('#{} {}'.format(tc, result))