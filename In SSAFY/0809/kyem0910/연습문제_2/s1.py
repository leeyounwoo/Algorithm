import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

# 1번 방법
# arr = []
# for _ in range(N):
#     arr.append(list(map(int,input().split())))

# 2번 방법 - list comprehension
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

# 행 우선 순회
print()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

# 열 우선 순회
print()
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end=" ")
    print()

# 역 행 우선 순회
print()
for i in range(len(arr)-1, -1, -1):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

# 역 열 우선 순회
print()
for i in range(len(arr[0])-1, -1, -1):
    for j in range(len(arr)):
        print(arr[j][i], end=" ")
    print()

# 지그재그
print()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j+(len(arr)-1-2*j) * (i%2)], end=" ")
    print()

