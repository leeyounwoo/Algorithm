import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    container_idx = 0
    truck_idx = 0
    truck_num = len(truck)
    container_num = len(container)
    result = 0
    while truck_idx < truck_num and container_idx < container_num:
        if container[container_idx] > truck[truck_idx]:
            container_idx += 1
        else:
            result += container[container_idx]
            container_idx += 1
            truck_idx += 1

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
