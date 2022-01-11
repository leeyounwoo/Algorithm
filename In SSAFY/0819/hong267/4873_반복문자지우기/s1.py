import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = input()
    s_list = [s[i] for i in range(len(s))] # 문자열을 리스트로 만들어 줌

    stack = []
    for i in range(len(s_list)):
        if len(stack) == 0: # 스택이 비어 있으면
            stack.append(s_list[i]) # 스택에 요소를 추가
        elif stack[-1] == s_list[i]: # 만약 스택의 마지막 요소가 s_list[i]와 같다면
            stack.pop() # 스택의 마지막 요소 제거
        else: # 그게 아니면 스택에 요소 추가
            stack.append(s_list[i])

    result = len(stack)
    print('#{0} {1}'.format(tc, result))