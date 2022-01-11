import sys
sys.stdin = open('input.txt')
# 부모를 저장하는 배열을 만들고
# 조가 만들어질 때 작업 번호를 가진 쪽으로 부모 병합

# find_set
# 어떤 원소 x가 속한 집합의 대표자를 반환하는 함수
# x를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])

# union
# 두 개의 상호 배타 집합을 합치는 연산
def union(x, y):    # 두 집합을 병합
    parents[find_set(x)] = find_set(y) # x를 y 뒤에 붙여

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 출석번호, 신청서 수
    data = list(map(int, input().split())) # M 쌍의 번호
    parents = [i for i in range(N+1)]

    # 한 쌍
    for i in range(0, M*2, 2):
        union(data[i], data[i+1])

    answer = []
    for i in range(1, N+1): # 0필요없음 1부터
        answer.append(find_set(i))

    print("#{} {}".format(tc, len(set(answer))))