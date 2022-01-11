import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, numbers = input().split()
    N = int(N)
    result = ''
    lst = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
           '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(N):
        num = lst[numbers[i]]
        ans = ''
        for _ in range(4):
            num, remainder = divmod(num, 2)
            ans += str(remainder)
        result += ans[::-1]
    print('#{} {}'.format(tc, result))
