import sys
sys.stdin = open('input.txt')

def binary_search(P, goal):
    l = 1
    r = P
    count = 0
    while l <= r:
        mid = int((l + r) / 2)
        if mid == goal:
            return count
        elif mid < goal:
            l = mid
            count += 1
        elif mid > goal:
            r = mid
            count += 1

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    count_A = binary_search(P, Pa)
    count_B = binary_search(P, Pb)

    if count_A > count_B:
        result = 'B'
    elif count_A < count_B:
        result = 'A'
    else:
        result = 0
    print('#{} {}'.format(tc, result))