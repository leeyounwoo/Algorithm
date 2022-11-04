def solution(m, n, puddles):
    array = [[0] * m for _ in range(n)]
    for i in range(n):
        array[i][0] = 1
    for j in range(m):
        array[0][j] = 1

    for puddle in puddles:
        index_j, index_i = puddle
        if index_i == 1:
            for j in range(index_j, m):
                array[0][j] = -1

        if index_j == 1:
            for i in range(index_i, n):
                array[i][0] = -1
        array[index_i-1][index_j-1] = -1

    for i in range(1, n):
        for j in range(1, m):
            # 물에 잠긴 경우
            if array[i][j] == -1:
                continue
            up = array[i-1][j]
            left = array[i][j-1]
            if up == -1 and left != -1:
                array[i][j] = left
            elif up != -1 and left == -1:
                array[i][j] = up
            elif up == -1 and left == -1:
                array[i][j] = -1
            elif up != -1 and left != -1:
                array[i][j] = (up + left) % 1000000007

    answer = array[n-1][m-1]
    if answer == -1:
        return 0

    return array[n-1][m-1]


print(solution(4, 3, [[1, 2], [2, 1]]))