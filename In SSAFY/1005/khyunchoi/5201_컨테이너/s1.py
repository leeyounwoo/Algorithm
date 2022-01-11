import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 컨테이너, M: 트럭
    container_list = list(map(int, input().split()))
    truck_list = list(map(int, input().split()))

    container_list.sort(reverse=True)
    truck_list.sort(reverse=True)

    result = 0
    for container in container_list:
        if truck_list and truck_list[0] >= container:
            result += container
            truck_list.pop(0)

    print('#{} {}'.format(tc, result))