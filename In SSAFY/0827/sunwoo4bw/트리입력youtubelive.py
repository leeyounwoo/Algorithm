'''
6
1 2 1 3 2 4 3 5 3 6
6
2 1 1 3 2 4 3 5 3 6
'''
def pre_order(n):
    global cnt
    if n :                  # 유효한 정점이면
        cnt += 1 # print(n)
        pre_order(left[n])  # n의 왼쪽자식으로 이동
        pre_order(right[n])

def in_order(n):
    if n :
        in_order(left[n])
        print(n)
        in_order(right[n])

def post_order(n):
    if n :
        post_order(left[n])
        post_order(right[n])
        print(n)

V = int(input())
edge = list(map(int, input().split()))
E = V -1   #V개의 정점이 있는 트리의 간선 수
left = [0] * (V+1)  # 부모를 인덱스로 자식 번호 저장
right = [0] * (V+1)
par = [0] * (V+1)  # 자식을 인덱스로 부모번호 저장

for i in range(E) :
    p, c = edge[i*2], edge[i*2 +1]
    if left[p] == 0: # p의 왼쪽자식이 없으면
        left[p] = c
    else:            # 왼쪽 자식이 있으면 오른쪽 자식으로 저장
        right[p] = c
    par[c] = p      # (1) 조상을 찾는데 사용
                    # (2) root 찾기

# c = 6  #의 조상
# while par[c] :
#     print(par[c])
#     c = par[c]

# 부모가 없으면 root
root = 1
while par[root] : # root로 추정한 정점이 부모가 있으면
    root += 1
print(root)

# cnt = 0
# pre_order(1)
# print(cnt)  # 3을 루트로하는 서브트리의 정점 개수
# print(cnt-1)  # 3의 자손의 수