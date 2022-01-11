import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    t, N = input().split()
    numbers = list(input().split())

    str_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    str_cnt = [0]*len(str_num)

    for number in numbers:
        for i in range(len(str_num)):
            if number == str_num[i]:
                str_cnt[i] += 1
                break

    result = []
    for j in range(len(str_num)):
        for _ in range(str_cnt[j]):
            result.append(str_num[j])

    print(t)
    print(' '.join(result))