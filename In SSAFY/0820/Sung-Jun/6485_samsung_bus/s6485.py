import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    bus_numbers = []
    for _ in range(N):
        A, B = map(int, input().split())
        bus_numbers.append((A, B))

    check_list = [0]*5001
    for bus_number in bus_numbers:
        for sum in range(bus_number[0],bus_number[1]+1):
            check_list[sum] += 1

    result = []
    P = int(input())
    for _ in range(P):
        result.append(check_list[int(input())])

    print('#{}'.format(tc+1), end=' ')
    print(*result)
