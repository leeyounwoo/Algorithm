'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(n):
    # 유효한 정점이면 (자식이 있으면)
    if n:
        print(n)
        pre_order(left[n]) # n의 왼쪽 자식으로 이동
        pre_order(right[n]) # n의 오른쪽 자식으로 이동


V = int(input())
E = V -1 # V개의 정점이 있는 트리의 간선 수
edge = list(map(int, input().split()))

# 부모를 인덱스로 자식 번호 저장
left = [0]*(V+1)
right = [0]*(V+1)

for i in range(E):
    p, c = edge[i*2], edge[i*2 + 1]
    # p의 왼쪽 자식이 없으면 왼쪽 자식으로 저장
    if left[p] == 0:
        left[p] = c
    # p의 왼쪽 자식이 있으면 오른쪽 자식으로 저장
    else:
        right[p] = c

pre_order(1)