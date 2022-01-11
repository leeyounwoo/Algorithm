import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

# 2차원 배열 입력 받기 - 첫 번째
# arr = []
# for _ in range(N) :
#     arr.append(list(map(int, input().split())))

# 2차원 배열 입력 받기 - 두 번째
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

# 1. 행 우선 순회
for i in range(len(arr)) :
    for j in range(len(arr[i])) :
        print(arr[i][j], end=' ')
    print()
print()

# 2. 열 우선 순회
for j in range(len(arr[0])) :
    for i in range(len(arr)) :
        print(arr[i][j], end=' ')
    print()
print()

# 3. 역-행 우선 순회
for i in range(len(arr)-1, -1, -1) :
    for j in range(len(arr[i])) :
        print(arr[i][j], end=' ')
    print()
print()

# 4. 역-열 우선 순회
for j in range(len(arr[0])-1, -1, -1) :
    for i in range(len(arr)) :
        print(arr[i][j], end=' ')
    print()
print()

# 5. 지그재그
for i in range(len(arr)) :
    for j in range(len(arr[i])):
        print(arr[i][j + (len(arr[0])-1-2*j) * (i%2)], end=' ')
    print()
