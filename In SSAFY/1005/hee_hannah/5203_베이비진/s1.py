import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    li = list(map(int, input().split()))

    a = []
    b = []
    for i in range(4): # 0~3 2씩만 먼저 분배
        if i % 2 == 0: # 0 2
            a.append(li[i])
        else: # 1 3
            b.append(li[i])
    li = li[4:] # 남은 8개
    # print(a, b, li) # [9, 5, 5] [9, 6, 6] [1, 1, 4, 2, 2, 1] # [5, 2, 1] [3, 9, 5] [2, 0, 9, 2, 0, 0]
    flag = 0
    while len(li) > 0:
        a.append(li.pop(0)) # 추가로 하나씩 더 담고
        b.append(li.pop(0))
        for j in a:
            if a.count(j) == 3: # 3개가 되면
                flag = 1
            if j+1 in a and j+2 in a: # 연속되면
                flag = 1
        if flag == 1:
            print(1) # 플레이어 1 승리
            break
        for k in b:
            if b.count(k) == 3:
                flag = 1
            if k+1 in b and k+2 in b:
                flag = 1
        if flag == 1: #플레이어 2 승리
            print(2)
            break

    if flag == 0: # 무승부
        print(0)

