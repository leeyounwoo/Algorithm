import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 입력받습니다.
T = int(input())

# 답을 저장할 리스트입니다.
answer = []
# 테스트 케이스 수 만큼 코드를 실행합니다.
for tc in range(1, T+1):
    # 처리할 후위계산식을 입력받습니다.
    seq = input().split()

    # 계산에 사용할 스택을 생성합니다.
    stack = []
    # 연산자의 모음을 생성합니다.
    # 이는 후위계산식에서 연산자를 구별할 때 사용합니다.
    operator = set({'+', '-', '*', '/'})
    # 잘못된 계산식일 경우 결과를 'error'로 설정하기 위해
    # try문을 이용합니다.
    try:
        # 후위계산식의 모든 문자를 탐색합니다.
        # 마지막 문자는 생략합니다.('.'이기 때문)
        for i in seq[:-1]:
            # 문자가 연산자라면
            # 그에 맞는 연산을 수행하고 스택에 푸시합니다.
            if i in operator:
                if i == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                elif i == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                elif i == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a // b)
            # 연산자가 아니라면 숫자로 변환해 스택에 푸시합니다.
            else:
                stack.append(int(i))
        # 연산이 끝나면 스택에는 최종 결과 한 개만이 남아있어야 합니다
        # 그게 아니라면 'error'입니다.
        if len(stack) == 1:
            result = stack[-1]
        else:
            result = 'error'
    # 연산 중간에 에러가 났다면 결과를 'error'로 바꿔줍니다.
    except IndexError:
        result = 'error'
    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc-1]))
