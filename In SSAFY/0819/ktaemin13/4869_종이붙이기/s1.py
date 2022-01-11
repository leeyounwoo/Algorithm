import sys
sys.stdin = open('input.txt')

stack = []

def is_empty():
    # 만약 스택의 길이가 0이면 True
    if len(stack) == 0:
        return True
    return False

def check_matching(paper):

    for i in range(len(paper)):
        if paper[i] == '(' or paper[i] == '{':
            stack.append(paper[i])
        elif paper[i] == ')' or paper[i] == '}':
            stack.pop()

    if not is_empty():
        return '0'
    return '1'

T = int(input())
for tc in range(T):
    paper = input()

    print('#{0} {1}'.format(tc+1, check_matching(paper)))