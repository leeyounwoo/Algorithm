import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 컨테이너 수, 트럭 수
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    trucks_check = [0] * M # 어떤 트럭에 어떤 컨테이너가 들어갈 것인지 체크해주는 리스트

    i = 0
    for container in containers:
        if trucks[i] >= container:
            trucks_check[i] = container
            i += 1
            if i > M-1: # 트럭이 꽉 찼다면 멈춰!
                break

    print('#{0} {1}'.format(tc, sum(trucks_check)))
