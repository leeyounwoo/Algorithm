import sys
sys.stdin = open('input.txt')
from collections import deque


for T in range(1, 1+int(input())):
    container_cnt, truck_cnt = map(int, input().split())
    a = [2, 1, 5]
    b = reversed(sorted(a))
    containers = deque(reversed(sorted(list(map(int, input().split())))))
    trucks = deque(reversed(sorted(list(map(int, input().split())))))
    # print('cotainers', containers)
    # print('trucks', trucks)
    ans = 0
    while trucks and containers:
        now_truck = trucks.popleft()
        now_container = containers.popleft()
        if now_truck >= now_container:
            ans += now_container
        else:
            trucks.appendleft(now_truck)
    print('#{} {}'.format(T, ans))