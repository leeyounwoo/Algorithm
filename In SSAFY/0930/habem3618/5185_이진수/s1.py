import sys
sys.stdin = open('input.txt')

T = int(input())
dec_to_hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, T+1):
    N, arr = input().split()
    result = []

    for i in arr[::-1]:

        if i in dec_to_hex:
            i = dec_to_hex[i]

        i = int(i)
        for _ in range(4):
            result.append(i % 2)
            i //= 2

    print("#{} {}".format(tc, ''.join(map(str, result[::-1]))))
