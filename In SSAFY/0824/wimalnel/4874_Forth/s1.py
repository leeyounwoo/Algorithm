import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    stack = []
    cal = list(input().split())
    Err = 0                     # ex) 10 2 + 3 4 + * .
                                # ex) 5 3 * + . == err
                                # ex) 1 5 8 10 3 4 + + 3 + * 2 + + + .

    for c in (cal[:-1]):     # 리스트의 맨 끝까지
        if c.isdigit():      # 숫자가 있는지 확인
            stack.append(c)  # 스택에 쌓는다
        else:
            try:            # 숫자가 더 이상 없다. 즉, 연산자다
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

            except:     #예외처리
                Err = -1

    if Err == -1 or len(stack) > 1: # 스택에 2개이상남으면 연산자가 모자라는 형식 error
        print('#{} {}'.format(tc, 'error'))

    elif Err == 0 and len(stack) == 1:
        print('#{} {}'.format(tc, int(stack[0])))