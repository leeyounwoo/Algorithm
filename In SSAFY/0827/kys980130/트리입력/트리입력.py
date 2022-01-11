import sys
sys.stdin = open("input.txt")

def pre_order(n):
    if n:       # 유효한 정점이면
        print(n)
        pre_order(left[n])      # n의 왼쪽 자식으로 이동
        pre_order(right[n])     # n의 오른쪽 자식으로 이동

V = int(input())
edge = list(map(int, input().split()))
E = V - 1   # V개의 정점이 있는 트리의 간선 수
left = [0] * (V+1)  # 부모를 인덱스로 자식번호 저장
right = [0] * (V+1)
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:    # p의 왼쪽 자식이 없으면
        left[p] = c
    else:               # 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c
pre_order(1)