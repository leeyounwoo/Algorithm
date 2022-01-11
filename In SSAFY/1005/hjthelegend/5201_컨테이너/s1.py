import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    # N개의 컨테이너, M대의 트럭
    # 컨테이너 마다 : 화물의 무게
    # 트럭 마다 : 적재 용량

    # 화물의 총 중량이 최대가 되도록
    # 옮겨진 화물의 전체 무게는 얼마인가?

    # 탐욕 알고리즘

    weight = list(map(int, input().split())) # 1 5 3
    trucks = list(map(int, input().split())) # 8 3 -> 빈공간 생겨도 됨

    # 1. 역순으로 정렬해서
    # 1-1. weight의 총합 구하고
    # 2. weight 큰것부터 truck 큰것에 -= 하고
    # 3. truck 못 들어간거 총합에서 빼기

    # 역순 정렬
    weight.sort(reverse=True) # 5 3 1
    trucks.sort(reverse=True) # 8 3
    # 큐 선언
    weight = deque(weight)

    total = sum(weight)

    for _ in range(len(weight)):
        loading = weight.popleft()
        for i in range(len(trucks)):
            if loading <= trucks[i]:
                trucks[i] = 0
                break
        else:
            weight.append(loading)

    total -= sum(weight)

    print('#{} {}'.format(tc, total))