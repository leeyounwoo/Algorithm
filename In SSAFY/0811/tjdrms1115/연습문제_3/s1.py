# 배열을 정렬하는 함수입니다. 선택 정렬을 사용했습니다.
def selection_sort(arr):

    n = len(arr)
    for i in range(n-1):
        tempmin = arr[i]
        idx = i
        for j in range(i+1, n):
            if tempmin > arr[j]:
                tempmin = arr[j]
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]


# 입력받은 배열입니다.
arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

# 출력 결과를 저장할 배열입니다.
new_arr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

# 입력 받은 2차원 배열을 편한 정렬을 위해 1차원 배열로 바꿉니다.
arr_1d = []
for line in arr:
    arr_1d += line

# 변환한 배열을 정렬합니다. 이제 순서대로 작은 값부터 꺼낼 수 있습니다.
selection_sort(arr_1d)

idx = 0
n = len(arr)
i, j = 0, 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
diridx = 0
diri, dirj = direction[diridx]
# 새 배열을 다 채울 때가지 반복합니다.
while idx < n*n:
    # 정렬된 arr_1d의 값을 순서대로 넣습니다.
    new_arr[i][j] = arr_1d[idx]
    idx += 1

    # 만약에 다음 위치가 막혔다면 방향을 바꿉니다.
    if (0 <= i + diri < n) and (0 <= j + dirj < n) and new_arr[i + diri][j + dirj] == 0:
        pass
    else:
        diridx = (diridx + 1) % 4

    # 방향을 지시합니다.
    diri, dirj = direction[diridx]

    # 다음 위치로 인덱스를 옮깁니다.
    i = i + diri
    j = j + dirj

# 완성된 배열을 출력합니다.
print(new_arr)
