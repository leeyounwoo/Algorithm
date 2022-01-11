import sys
sys.stdin = open('input.txt')

def get_pos(num):
    if num % 2:
        return (num + 1) // 2
    else:
        return num // 2

TC = int(input())
for tc in range(TC):
    corridor = [0 for _ in range(201)]
    num = int(input())
    for _ in range(num):
        curr, target = map(int, input().split())
        curr = get_pos(curr)
        target = get_pos(target)

        if curr > target:
            curr, target = target, curr

        for i in range(curr, target + 1):
            corridor[i] += 1

    print('#{} {}'.format(tc+1, max(corridor)))
