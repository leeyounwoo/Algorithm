import sys
sys.stdin = open("input.txt")

T = int(input())

for T in range(1, T+1):
    a = input().split()
    b = input().split()
    len_a = len(a)
    len_b = len(b)
    key = len_a - len_b

    print('#{} {}'.format(T, key))
