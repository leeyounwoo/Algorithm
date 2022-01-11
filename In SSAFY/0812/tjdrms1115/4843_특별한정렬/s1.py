import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):

    # 숫자의 개수 및 숫자 리스트를 입력받습니다.
    N = int(input())
    numbers = list(map(int, input().split()))

    # 특별한 정렬을 실행합니다. 선택 정렬로 합니다.
    for i in range(N):
        idx = i

        # 홀수 번째 인덱스는 오름차순으로 정렬합니다.
        if i % 2:
            for j in range(i+1, N):
                if numbers[idx] > numbers[j]:
                    idx = j
        # 짝수 번째 인덱스는 내림차순으로 정렬합니다.
        else:
            for j in range(i+1, N):
                if numbers[idx] < numbers[j]:
                    idx = j
        numbers[i], numbers[idx] = numbers[idx], numbers[i]

    # 결과를 10번째 까지만 출력합니다.
    answer.append(numbers[:10])


for tc in range(1, T+1):
    print('#{0}'.format(tc),  *answer[tc-1])
