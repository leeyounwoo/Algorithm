def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    clock_true_up = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    clock_true_right = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    clock_true_down = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    clock_true_left = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    clock_false_up = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    clock_false_right = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    clock_false_down = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    clock_false_left = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    # 홀수, 한 점에서 시작
    if n % 2:
        temp = [2]
        for i in range((n - 3)//2):
            temp.append(temp[-1] + 2)
        cnt = sum(temp) + 1
        start_i, start_j = n // 2, n // 2
        answer[start_i][start_j] = cnt
        # 위쪽 순회
        temp.insert(0, 1)
        rotate_up = 0
        rotate_left = 0
        rotate_down = 0
        rotate_right = 0
        if not clockwise:
            cnt_up = cnt
            cnt_left = cnt
            cnt_down = cnt
            cnt_right = cnt
            start_i_up = start_i
            start_j_up = start_j
            start_i_left = start_i
            start_j_left = start_j
            start_i_down = start_i
            start_j_down = start_j
            start_i_right = start_i
            start_j_right = start_j
            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_up -= 1
                    if not cnt_up:
                        break
                    start_i_up += clock_false_up[rotate_up][0]
                    start_j_up += clock_false_up[rotate_up][1]
                    answer[start_i_up][start_j_up] = cnt_up
                rotate_up = (rotate_up + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_left -= 1
                    if not cnt_left:
                        break
                    start_i_left += clock_false_left[rotate_left][0]
                    start_j_left += clock_false_left[rotate_left][1]
                    answer[start_i_left][start_j_left] = cnt_left
                rotate_left = (rotate_left + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_down -= 1
                    if not cnt_down:
                        break
                    start_i_down += clock_false_down[rotate_down][0]
                    start_j_down += clock_false_down[rotate_down][1]
                    answer[start_i_down][start_j_down] = cnt_down
                rotate_down = (rotate_down + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_right -= 1
                    if not cnt_right:
                        break
                    start_i_right += clock_false_right[rotate_right][0]
                    start_j_right += clock_false_right[rotate_right][1]

                    answer[start_i_right][start_j_right] = cnt_right
                rotate_right = (rotate_right + 1) % 4

        else:
            cnt_up = cnt
            cnt_left = cnt
            cnt_down = cnt
            cnt_right = cnt
            start_i_up = start_i
            start_j_up = start_j
            start_i_left = start_i
            start_j_left = start_j
            start_i_down = start_i
            start_j_down = start_j
            start_i_right = start_i
            start_j_right = start_j
            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_up -= 1
                    if not cnt_up:
                        break
                    start_i_up += clock_true_up[rotate_up][0]
                    start_j_up += clock_true_up[rotate_up][1]
                    answer[start_i_up][start_j_up] = cnt_up
                rotate_up = (rotate_up + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_left -= 1
                    if not cnt_left:
                        break
                    start_i_left += clock_true_left[rotate_left][0]
                    start_j_left += clock_true_left[rotate_left][1]
                    answer[start_i_left][start_j_left] = cnt_left
                rotate_left = (rotate_left + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_down -= 1
                    if not cnt_down:
                        break
                    start_i_down += clock_true_down[rotate_down][0]
                    start_j_down += clock_true_down[rotate_down][1]
                    answer[start_i_down][start_j_down] = cnt_down
                rotate_down = (rotate_down + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_right -= 1
                    if not cnt_right:
                        break
                    start_i_right += clock_true_right[rotate_right][0]
                    start_j_right += clock_true_right[rotate_right][1]

                    answer[start_i_right][start_j_right] = cnt_right
                rotate_right = (rotate_right + 1) % 4


    else:
        rotate_up = 0
        rotate_left = 0
        rotate_down = 0
        rotate_right = 0
        if not clockwise:
            temp = [3]
            for i in range((n - 3) // 2):
                temp.append(temp[-1] + 2)
            cnt = sum(temp) + 1
            temp.insert(0, 1)

            cnt_up = cnt
            cnt_left = cnt
            cnt_down = cnt
            cnt_right = cnt
            start_i_up = n // 2 - 1
            start_j_up = n // 2 - 1
            answer[start_i_up][start_j_up] = cnt
            start_i_left = n // 2
            start_j_left = n // 2 - 1
            answer[start_i_left][start_j_left] = cnt
            start_i_down = n // 2
            start_j_down = n // 2
            answer[start_i_down][start_j_down] = cnt
            start_i_right = n // 2 - 1
            start_j_right = n // 2
            answer[start_i_right][start_j_right] = cnt

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_up -= 1
                    if not cnt_up:
                        break
                    start_i_up += clock_false_up[rotate_up][0]
                    start_j_up += clock_false_up[rotate_up][1]
                    answer[start_i_up][start_j_up] = cnt_up
                rotate_up = (rotate_up + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_left -= 1
                    if not cnt_left:
                        break
                    start_i_left += clock_false_left[rotate_left][0]
                    start_j_left += clock_false_left[rotate_left][1]
                    answer[start_i_left][start_j_left] = cnt_left
                rotate_left = (rotate_left + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_down -= 1
                    if not cnt_down:
                        break
                    start_i_down += clock_false_down[rotate_down][0]
                    start_j_down += clock_false_down[rotate_down][1]
                    answer[start_i_down][start_j_down] = cnt_down
                rotate_down = (rotate_down + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_right -= 1
                    if not cnt_right:
                        break
                    start_i_right += clock_false_right[rotate_right][0]
                    start_j_right += clock_false_right[rotate_right][1]

                    answer[start_i_right][start_j_right] = cnt_right
                rotate_right = (rotate_right + 1) % 4

        else:
            temp = [3]
            for i in range((n - 3) // 2):
                temp.append(temp[-1] + 2)
            cnt = sum(temp) + 1
            temp.insert(0, 1)
            cnt_up = cnt
            cnt_left = cnt
            cnt_down = cnt
            cnt_right = cnt
            start_i_left = n // 2 - 1
            start_j_left = n // 2 - 1

            start_i_down = n // 2
            start_j_down = n // 2 - 1

            start_i_right = n // 2
            start_j_right = n // 2

            start_i_up = n // 2 - 1
            start_j_up = n // 2

            answer[start_i_down][start_j_down] = cnt
            answer[start_i_left][start_j_left] = cnt
            answer[start_i_up][start_j_up] = cnt
            answer[start_i_right][start_j_right] = cnt
            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_up -= 1
                    if not cnt_up:
                        break
                    start_i_up += clock_true_up[rotate_up][0]
                    start_j_up += clock_true_up[rotate_up][1]
                    answer[start_i_up][start_j_up] = cnt_up
                rotate_up = (rotate_up + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_left -= 1
                    if not cnt_left:
                        break
                    start_i_left += clock_true_left[rotate_left][0]
                    start_j_left += clock_true_left[rotate_left][1]
                    answer[start_i_left][start_j_left] = cnt_left
                rotate_left = (rotate_left + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_down -= 1
                    if not cnt_down:
                        break
                    start_i_down += clock_true_down[rotate_down][0]
                    start_j_down += clock_true_down[rotate_down][1]
                    answer[start_i_down][start_j_down] = cnt_down
                rotate_down = (rotate_down + 1) % 4

            for t in range(len(temp)):
                for z in range(temp[t]):
                    cnt_right -= 1
                    if not cnt_right:
                        break
                    start_i_right += clock_true_right[rotate_right][0]
                    start_j_right += clock_true_right[rotate_right][1]

                    answer[start_i_right][start_j_right] = cnt_right
                rotate_right = (rotate_right + 1) % 4

    return answer

print(solution(6, True))
print(solution(6, True))
print(solution(9, True))
print(solution(9, False))
