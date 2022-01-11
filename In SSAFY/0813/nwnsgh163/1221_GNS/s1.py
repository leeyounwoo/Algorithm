import sys
sys.stdin = open('input.txt')

T = int(input())

def bubble_sort(num):
    for i in range(len(num)-1, 0, -1):		# 범위의 끝 위치
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num


for tc in range(1, T+1):
    N, len = input().split()
    string = list(input().split())


    s = ("ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN")


    new = []
    for i in range(int(len)):
        new.append(s.index(string[i]))        # 각 인덱스 번호가 리스트에 적어짐

    new.sort()

    for j in range(int(len)):
        new[j] = s[new[j]]

    print('#{}'.format(N))
    print(*new)
