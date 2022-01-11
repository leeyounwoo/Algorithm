import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    P, A, B = map(int, input().split())
    l = 1
    r = P
    a_count = b_count = 0
    while l <= r:
        c = (l + r) // 2
        if c == A:
            a_count += 1
            break
        if c > A:
            r = c
            a_count += 1
        else:
            l = c
            a_count += 1

    l = 1
    r = P
    while l <= r:
        c = (l + r) // 2
        if c == B:
            b_count += 1
            break
        if c > B:
            r = c
            b_count += 1
        else:
            l = c
            b_count += 1

    if a_count < b_count:
        print("#{} A".format(tc+1))
    elif a_count > b_count:
        print("#{} B".format(tc+1))
    else:
        print("#{} 0".format(tc+1))

