import sys
sys.stdin = open('input.txt')


# 스택 푸시
def push(item):
    stack.append(item)


# 스택 팝
def pop():
    if is_empty():
        return None
    return stack.pop()


# 스택이 비어있는지 검사하는 함수
def is_empty():
    if len(stack) == 0:
        return True
    return False


T = int(input())

answer = []
for tc in range(1, T+1):
    # 스택을 초기화합니다.
    stack = []
    # 문자열을 입력받습니다.
    line = input()

    # 여는 괄호 및 닫는 괄호의 모음입니다.
    open_braces = ['(', '{']
    close_braces = [')', '}']

    result = 0
    for char in line:
        # 문자가 여는 괄호에 속하면 스택에 푸시합니다.
        if char in open_braces:
            push(char)
        # 문자가 닫는 괄호에 속하면 스택에서 팝하고
        # 팝한 결과가 서로 짝을 이루는 지 검사합니다.
        elif char in close_braces:
            idx = close_braces.index(char)
            if open_braces[idx] != pop():
                break
    # 중간에 문제가 없었다면,
    # 문자열을 다 탐색하고 나서 스택이 비어있는지 검사합니다.
    # 스택이 비어있으면 성공입니다.
    else:
        if is_empty():
            result = 1

    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
