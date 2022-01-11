import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    queue = []
    for i in li:
        queue.append(i)

    while queue[-1] != 0:
        for k in range(1, 6):
            num = queue.pop(0)
            if num - k <= 0:
                num = 0
                queue.append(num)
                break
            elif num - k > 0:
                queue.append(num - k)
    print('#{}'.format(tc), end=' ')
    for i in queue:
        print('{}'.format(i), end=' ')
    print()
