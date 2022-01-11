import sys

sys.stdin = open('input.txt')
for T in range(1, int(input()) + 1):
    total, page_a, page_b = map(int, input().split())
    ans = 0
    l_a = 1
    r_a = total
    l_b = 1
    r_b = total

    find_a = 0
    find_b = 0
    while find_a != page_a and find_b != page_b:
        find_a = (l_a + r_a) // 2
        if find_a > page_a:
            r_a = find_a
        elif find_a < page_a:
            l_a = find_a
        else:
            ans = 'A'

        find_b = (l_b + r_b) // 2
        if find_b > page_b:
            r_b = find_b
        elif find_b < page_b:
            l_b = find_b
        # 이번 반복에서 A도 찾고 B도 찾은 경우엔 동점.
        else:
            if ans == 'A':
                ans = 0
            else:
                ans = 'B'

    print('#{} {}'.format(T, ans))