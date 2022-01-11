import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    answer = 1
    for puzzle_width in puzzle:
        check_list = [0 for _ in range(10)]
        for i in range(1, 10):
            if i in puzzle_width:
                check_list[i] += 1
        if 0 in check_list[1:]:
            answer = 0
            break

    puzzle_vertical = []
    for i in range(9):
        temp = []
        for puzzle_height in puzzle:
            temp.append(puzzle_height[i])
        puzzle_vertical.append(temp)

    for vertical in puzzle_vertical:
        check_list = [0 for _ in range(10)]
        for i in range(1, 10):
            if i in vertical:
                check_list[i] += 1
        if 0 in check_list[1:]:
            answer = 0
            break

    puzzle_square = []
    i = [0, 1, 2]
    for a in i:
        for b in i:
            for c in i:
                temp = []
                for line in puzzle[c * 3:(c + 1) * 3]:
                    for n in line[b * 3:(b + 1) * 3]:
                        temp.append(n)
                puzzle_square.append(temp)

    for square in puzzle_square:
        check_list = [0 for _ in range(10)]
        for i in range(1, 10):
            if i in square:
                check_list[i] += 1
        if 0 in check_list[1:]:
            answer = 0
            break

    print(f'#{tc + 1} {answer}')