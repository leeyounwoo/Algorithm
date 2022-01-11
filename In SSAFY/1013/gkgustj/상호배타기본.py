# make_set
def make_set(x):
    parents[x] = x


# find_set : 어떤 원소 x가 속한 집합의 대표자를 반환
def find_set(x):
    if x == parents[x]:
        return x

    return find_set(parents[x])


# union : 두 개의 상호 배타 집합을 합치는 연산
# 1) 두 집합의 대표자를 찾아서
# 2) 한 쪽의 대표자를 반대쪽의 대표자 바로 밑에 붙이기
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 대표자가 같을 경우 이미 같은 집합에 속해있음
    if root_x == root_y:
        return False

    parents[root_y] = root_x
    return True


nodes = [1, 2, 3, 4, 5, 6]
parents = [0] * (len(nodes) + 1)  # 각 노드의 부모 저장

for node in nodes:
    make_set(node)

union(1, 3)
print('1의 대표', find_set(1))  # 1
print('3의 대표', find_set(3))  # 1
print(parents)

union(2, 3)
print('1의 대표', find_set(1))  # 2
print('2의 대표', find_set(2))  # 2
print('3의 대표', find_set(3))  # 2
print(parents)

union(4, 3)
print('4의 대표', find_set(2))  # 4
print('3의 대표', find_set(3))  # 4
print(parents)

union(5, 3)
print('5의 대표', find_set(5))  # 5
print('3의 대표', find_set(3))  # 5
print(parents)

union(6, 3)
print('1의 대표', find_set(1))  # 6
print('2의 대표', find_set(2))  # 6
print('3의 대표', find_set(3))  # 6
print('4의 대표', find_set(4))  # 6
print('5의 대표', find_set(5))  # 6
print('6의 대표', find_set(6))  # 6
print(parents)