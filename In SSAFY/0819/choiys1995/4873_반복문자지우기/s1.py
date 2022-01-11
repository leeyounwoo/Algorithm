import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []
    for i in range(len(string)):
        # 스택에 아무것도 없거나 비교할 문자가 스택 마지막 문자랑 다르면
        if not len(stack) or string[i] != stack[-1]:
            stack.append(string[i])
        else:
            stack.pop()

    print('#{} {}'.format(T, len(stack)))