import sys
sys.stdin = open('input.txt')

stack = []

def is_empty():
    # 만약 스택의 길이가 0이면 True
    if len(stack) == 0:
        return True
    return False

def check_matching(test):

    for i in range(len(test)):
        if test[i] == '(' or test[i] == '{':
            stack.append(test[i])
        elif stack and test[i] == test[i-1] == ')' or test[i] == test[i-1] == '}':
            stack.pop()

    if not is_empty():
        return 0
    return 1

T = int(input())
for tc in range(T):
    test = input()

    print('#{0} {1}'.format(tc+1, check_matching(test)))