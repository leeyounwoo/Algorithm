import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    stack = []
    cal = list(input().split())

    for c in (cal[:-1]):     # 리스트의 맨 끝까지
        if c.isdigit():      # 숫자가 있는지 확인
            stack.append(c)  # 스택에 쌓는다
        else:
                a = int(stack.pop())
                b = int(stack.pop())

                if c == "+":
                    result = b+a
                elif c == "-":
                    result = b-a  # 후위 표기법이고 스택에 pop한 순서이므로
                elif c == "*":
                    result = b*a
                elif c == "/":
                    result = b/a
                stack.append(result)

        print('#{} {}'.format(tc, int(stack[0])))