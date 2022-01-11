import sys
sys.stdin = open('input.txt')

#find_set: x를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == parent[x]:
        return x
    return find_set(parent[x])
# x와 y를 포함하는 두 집합을 통합하는 연산
def union(x, y):
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int,input().split()))
    # 출석번호 인덱스까지 parent 리스트 만들어주기(0번은 사용안함)
    # 부모를 자기 자신으로 정의
    parent = [i for i in range(N + 1)]

    # 두개씩잘라서 한 쌍마다 union연산 해준다.
    for i in range(0, len(lst), 2):
        union(lst[i], lst[i+1])

    result = set()

    for i in range(1, N + 1):
        result.add(find_set(i))

    print("#{} {}".format(tc, len(result)))