import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    a = input()
    arr = [0] * 10

    for i in a:
        arr[int(i)] += 1

    max_card = arr[9]
    idx = 9
    for i in range(8, -1, -1):
        if arr[i] > max_card:
            max_card = arr[i]
            idx = i

    print("#{} {} {}".format(tc + 1, idx, max_card))