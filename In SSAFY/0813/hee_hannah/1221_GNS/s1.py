import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T+1):
    dic = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    tc, len_num = map(str, input().split())
    print(tc)
    total = []
    words = list(map(str, input().split()))
    for word in words:
        a = dic[word]
        total.append(a)

    fin = sorted(total)

    for key, value in dic.items():
        for i in fin:
            if i == value:
                print(key, end=" ")

