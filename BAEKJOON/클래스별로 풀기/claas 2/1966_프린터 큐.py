import sys

sys.stdin = open('input.txt')

for t in range(int(input())):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    meta_bus = [False for _ in range(n)]
    meta_bus[m] = True
    start = 0
    ans = 1
    while queue:
        if queue.count(max(queue)) == 1:
            queue = queue[start:] + queue[:start]
            meta_bus = meta_bus[start:] + meta_bus[:start]
            start = queue.index(max(queue))
            if meta_bus[start]:
                break
            queue.pop(start)
            meta_bus.pop(start)
            ans += 1
            start %= len(queue)
        else:
            queue = queue[start:] + queue[:start]
            meta_bus = meta_bus[start:] + meta_bus[:start]
            start = queue.index(max(queue))
            if meta_bus[start]:
                break
            queue.pop(start)
            meta_bus.pop(start)
            ans += 1
            start %= len(queue)

    print(ans)