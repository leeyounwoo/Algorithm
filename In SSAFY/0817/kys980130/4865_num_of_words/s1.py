import sys
sys.stdin = open("input.txt")
N = int(input())
for tc in range(1, N+1):
    str1 = list(set(input()))
    str2 = input()
    check = [0] * len(str1)
    max_num = 0
    for i in str1:
        for j in range(len(str2)):
            if str2[j] == i:
                check[str1.index(i)] += 1
    for n in check:
        if n > max_num:
            max_num = n
    print('#{} {}'.format(tc, max_num))