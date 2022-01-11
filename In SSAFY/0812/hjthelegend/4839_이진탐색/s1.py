import sys
sys.stdin = open('input.txt')

t = int(input())


def binary_search(page, key):
    start = 1
    end = page
    cnt = 1

    while start <= end:
        middle = int((start + end) / 2)
        if middle == key:
            return cnt
        cnt += 1

        if middle > key:
            end = middle
        else:
            start = middle
    return 0


for tc in range(1, t + 1):
    p, pa, pb = map(int, input().split())


    if binary_search(p, pa) < binary_search(p, pb):
        print('#{0} A'.format(tc))
    elif binary_search(p, pa) == binary_search(p, pb):
        print('#{0} 0'.format(tc))
    else:
        print('#{0} B'.format(tc))