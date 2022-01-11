import sys
sys.stdin = open('input.txt')

# T = int(input())
# 테스트 케이스의 개수를 입력받습니다. 이번 문제에서는 고정값이 주어집니다.
T = 10

# 테스트 케이스만큼 코드를 실행해 저장합니다.
answer = []
for tc in range(1, T+1):

    # 테스트 케이스 번호와 숫자열을 입력받습니다. testcase 변수는 쓰지 않습니다.
    testcase = int(input())
    numbers = list(map(int, input().split()))

    # 문제의 사이클은 8사이클을 돌때마다
    # 모든 숫자가 제위치로 돌아오면서
    # 동시에 숫자의 값이 15만큼 줄어듭니다.
    # 따라서 모든 숫자가 15보다 크면
    # 최소 한 숫자가 15이하가 되도록 전체 숫자의 값을 줄여줍니다.
    # 이 때 줄이기 위해 빼주는 값은 15의 배수입니다.

    # 숫자열의 최솟값을 찾습니다.
    minnum = min(numbers)
    # 최솟값을 바탕으로 각 배열에 빼줄 숫자를 계산합니다.
    common_sub = ((minnum // 15) - 1) * 15
    # 숫자열의 각 숫자에 위에서 구한 값을 빼줍니다.
    for i in range(len(numbers)):
        numbers[i] -= common_sub

    # 초기 설정 후 사이클을 돌립니다.
    # 초기 사이클은 1에서부터 시작합니다.
    # 이를 위한 변수 cycle을 초기화합니다.
    cycle = 0
    # 어느 한 숫자가 0이 될 때까지 반복합니다.
    while True:
        # 숫자열의 맨 앞의 숫자를 빼줍니다.
        num = numbers.pop(0)
        # 그 숫자에 사이클 횟수에 따라 알맞는 값을 빼줍니다.
        num -= cycle + 1
        # 만약에 계산 결과가 0이하라면 0을 마지막 자리에 넣고 반복을 종료합니다.
        if num <= 0:
            numbers.append(0)
            break
        # 아니라면 계산 결과를 마지막 자리에 넣고 반복합니다.
        numbers.append(num)
        # 사이클 변수를 조정합니다.
        cycle = (cycle + 1) % 5

    # 최종 결과를 출력합니다.
    answer.append(numbers)

for tc in range(1, T+1):
    print('#{}'.format(tc), *answer[tc-1])
