import math

def count(start_i, start_j, end_i, end_j):
    width = abs(start_i - end_i)
    height = abs(start_j - end_j)

    return math.factorial(width + height) // (math.factorial(width) * math.factorial(height))

def solution(width, height, diagonals):
    answer = 0
    num = 10000019
    goal_i = height
    goal_j = width

    for i in range(len(diagonals)):
        diagonals[i][0], diagonals[i][1] = diagonals[i][0] - 1, diagonals[i][1] - 1

    for i in range(len(diagonals)):

        mid_i_1 = diagonals[i][0] + 1
        mid_j_1 = diagonals[i][1]
        cnt_1 = count(0, 0, mid_i_1, mid_j_1) * count(mid_i_1, mid_j_1, goal_i, goal_j) % num

        mid_i_2 = diagonals[i][0]
        mid_j_2 = diagonals[i][1] + 1
        cnt_2 = (count(0, 0, mid_i_2, mid_j_2) * count(mid_i_2, mid_j_2, goal_i, goal_j)) % num

        answer += (cnt_1 + cnt_2) % num


    return answer


print(solution(2, 2, [[1, 1], [2, 2]]))
print(solution(51, 37, [[17, 19]]))