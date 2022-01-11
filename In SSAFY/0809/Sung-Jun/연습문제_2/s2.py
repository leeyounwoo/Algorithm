import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

# arr =[]
# for _ in range(N):
#     arr.append(list(map(int, input().split())))
# print(arr)

arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
#
# #열 우선
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j], end =" ")
#     print()
#
# for i in range(len(arr)):
#     for j in range(len(arr[0])-1, -1, -1):
#         print(arr[i][j], end=" ")
#     print()
#
# for i in range(len(arr[0])-1, -1, -1):
#     for j in range(len(arr)):
#         print(arr[i][j], end = " ")
#     print()

for i in range(len(arr)):
    if i%2 == 0:
        for j in range(len(arr[0])):
            print(arr[i][j], end = " ")
    else:
        for j in range(len(arr[0])-1, -1, -1):
            print(arr[i][j], end=" ")
    print()
