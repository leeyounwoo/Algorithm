import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T+1):

    # 입력값을 입력받습니다.
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 출력될 결과를 인덱스로만 확인해줍니다.
    # 순환하기 때문에 M%N번째 인덱스의 결과가 정답입니다.
    result = numbers[M % N]
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
