import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split()) # N=3, M=4

# 2차원 입력 받기_1
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))

# 2차원 입력 받기_2

arr = [list(map(int, input().split())) for i in range(N)]

print(arr)

# 1. 행 우선 순회
'''
[
    [0, 1, 2, 3 ],
    [4, 5, 6, 7 ],
    [8, 9, 10, 11 ],
]
0 1 2 3 4 5 6 7 8 9 10 11
'''
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end=' ')
#     print()
#
# # 2. 열 우선 순회
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j], end=' ')
#     print()

# 3. 역행 우선순회
# for i in range(len(arr)):
#     for j in range(len(arr[0])-1, -1, -1):
#         print(arr[i][j], end=' ')
#     print()

# 4. 역-열 우선순회
# for i in range(len(arr[0])-1, -1, -1):
#     for j in range(len(arr)):
#         print(arr[j][i], end=' ')
#     print()

# 5. 지그재그 순회
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j + (len(arr)-1-2*j) * (i % 2)], end=' ')
#    print()