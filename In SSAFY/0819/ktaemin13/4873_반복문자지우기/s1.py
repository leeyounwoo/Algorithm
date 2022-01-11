import sys
sys.stdin = open('input.txt')

def check_matching(chr):               # 입력받은 문자열을 하나씩 꺼내옴
    stack = []                         # 스택 초기화
    for i in chr:
        if stack and i == stack[-1]:   # 1. 스택이 비어있지 않고,
            stack.pop()                # 2. i와 stack[-1]이 같으면, pop
        else:
            stack.append(i)            # 3. 다르면 append(i)
    return len(stack)                  # 4. 길이 출력

T = int(input())
for tc in range(T):
    chr = input()
    print('#{0} {1}'.format(tc+1, check_matching(chr)))