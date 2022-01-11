import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    print('#{}'.format(tc))
    a = int(input()) #4 라고한다면

    b = [[0]*a for _ in range(a)] # a만큼 빈 리스트 만들어두기
    for i in range(a): # i = 0 1 2 3 x축
        for j in range(a): # y축
            if i == j or j == 0: #규칙...
                b[i][j] = 1
            else:
                b[i][j] = b[i-1][j] + b[i-1][j-1] #내 위 + 내위의 왼쪽
    for k in range(len(b)): # 0 1 2 3
        c = b[k][:k+1] # 0들 버리고 필요한 부분만 잘라내기
        print(*c) # 리스트 풀기







