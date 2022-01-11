import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0] * 5

    for idx, value in enumerate([2, 3, 5, 7, 11]):
        while True:
            if N % value == 0:
                N = N / value
                arr[idx] += 1
            else:
                break

    print("#{} {}".format(tc + 1, ' '.join(map(str, (arr)))))