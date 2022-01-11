import sys
sys.stdin = open('input.txt')


# make_set
def make_set(x):
    parents[x] = x # 자기 자신 대표만들기

# find_set
# 어떤 원소 x 가 속한 집합의 대표자를 반환하는 함수
def find_set(x):
    if x == parents[x]: # 부모가 자기 자신이면 루트
        return x
    return find_set(parents[x])

def union(x, y):
    root_x = find_set(x) # 각각의 부모를 변수에 담아줌
    root_y = find_set(y)
    # 대표자가 같을 경우 이미 같은 집합에 속해있음
    if root_x == root_y:
        return False

    parents[root_y] = root_x # y의 부모를 x로 바꿔줌
    return True

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    li = list(map(int, input().split())) # 1 2 3 4
    parents = [0] * (n + 1)  # 각 노드의 부모 저장

    for i in range(1, n+1):
        make_set(i) # 0 1 2 3 4 5 셀프 대표

    for j in range(1, len(li)+1, 2): # 1 2, 3 4 -> 1, 3
        # parents[li[j]] = li[j-1]
        s = li[j-1] # li[0] = 1
        e = li[j] # li[1] = 2 2의 부모는 1
        union(s, e) # 합체

    total = []
    for k in parents:
        a = find_set(k)
        if a not in total:
            total.append(a) # 중복되지 않게 대표 담기

    print('#{} {}'.format(tc, len(total)-1)) # 0이 포함되기때문에 -1
