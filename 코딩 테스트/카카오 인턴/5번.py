from copy import deepcopy


def shift(array):
    temp = [array[-1]]
    temp += array[:-1]
    return temp


def rotate(array):
    temp = [[array[1][0]] + array[0][:-1]]
    temp += array[1:-1]
    temp += [array[-1][:-1] + [array[-2][-1]]]

    for i in range(1, len(array) - 1):
        temp[i][0] = array[i+1][0]
        temp[i][len(array[0])-1] = array[i-1][len(array[0])-1]

    return temp


def solution(rc, operations):
    for command in operations:
        if command == "Rotate":
            rc = rotate(rc)
        else:
            rc = shift(rc)

    return rc


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
# print(solution())
# print(solution())
# print(solution())

