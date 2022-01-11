import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    n = int(input())
    boxs = list(map(int, input().split()))
    ans = 0
    for i in range(len(boxs) - 1):
        count = 0
        for j in range(i + 1, len(boxs)):
            if boxs[i] > boxs[j]:
                count += 1
            else:
                break
        if ans < count:
            ans = count

    print('#{} {}'.format(T, ans))