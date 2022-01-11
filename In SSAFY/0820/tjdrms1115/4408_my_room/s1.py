import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    # 사람의 숫자를 입력받습니다.
    N = int(input())

    # 복도의 크기입니다. 최대 크기로 잡습니다.
    corridor = [0] * 201

    # 모든 사람의 경로를 확인합니다.
    for _ in range(N):
        # 각 사람의 시작 위치와 끝 위치를 입력받습니다.
        a, b = map(int, input().split())
        # 편한 계산을 위해 정렬해줍니다.
        if a > b:
            a, b = b, a
        # a 와 b 사이에 해당하는 복도에 지나간 횟수를 더합니다.
        for i in range((a+1)//2, ((b+1)//2)+1):
            corridor[i] += 1

    # 경로가 겹친 최대 횟수가 곧 학생들이 돌아갈 수 있는 최소 횟수입니다.
    result = max(corridor)

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
