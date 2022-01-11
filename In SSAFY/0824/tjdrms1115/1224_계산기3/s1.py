import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 입력받습니다. 고정값입니다.
T = 10

# 답을 저장할 리스트입니다.
answer = []
# 테스트 케이스 수 만큼 코드를 실행합니다.
for tc in range(1, T + 1):

    # 중위연산을 할 문자열의 길이와 연산 대상 문자열을 입력받습니다.
    N = int(input())
    seq = input()

    # 빈 스택을 생성합니다.
    stack = []
    # 문자열에서 숫자를 분리하기 위한 리스트입니다.
    digits = '0123456789'
    # 스택 안팎으로 우선순위를 결정하는 딕셔너리입니다.
    operator_outer = {
        '+': 1,
        '*': 2,
        '(': 3
    }
    operator_inner = {
        '(': 0,
        '+': 1,
        '*': 2,
    }

    # 후위계산식으로 변형합니다.
    postfix = ''
    for i in seq:
        # 입력받은 문자가 숫자라면 바로 후위계산식에 추가합니다.
        if i in digits:
            postfix += i
        # 숫자가 아니라면 스택을 이용하여 작업합니다.
        # 닫는 괄호라면 여는 괄호 직전까지
        # 모든 연산자를 스택에서 팝하여 후위계산식에 추가하고
        # 마지막으로 여는 괄호를 팝하여 없앱니다.
        elif i == ')':
            while len(stack) > 0 and operator_inner[stack[-1]] > operator_inner['(']:
                postfix += stack.pop()
            stack.pop()
        # 위의 경우 이외라면
        # 우선순위에 맞게 스택에 집어넣습니다.
        # 특정 연산자가 들어갈 때, 우선 스택의 맨 위에 있는 연산자가
        # 들어가려는 연산자보다 우선순위가 낮을 때까지 스택에서 팝하여
        # 후위계산식에 추가합니다.
        else:
            while len(stack) > 0 and operator_outer[i] <= operator_inner[stack[-1]]:
                postfix += stack.pop()
            stack.append(i)

    while stack:
        postfix += stack.pop()

    # 이제 후위계산식을 통해 최종 계산을 진행합니다.
    # 후위계산식의 모든 문자를 탐색합니다.
    for i in postfix:
        # 문자가 숫자라면 스택에 푸시합니다.
        if i in digits:
            stack.append(int(i))
        # 숫자가 아니라면 알맞은 계산을 하여 결과를 스택에 푸시합니다.
        else:
            if i == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

    # 스택에 남은 마지막 숫자가 결과입니다.
    # 이를 출력합니다.
    result = stack[-1]
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc - 1]))
