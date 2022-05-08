def solution(line):
    answer = []
    keyboard_i = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0,
                  "Q": 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1}
    keyboard_j = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '0': 9,
                  "Q": 0, 'W': 1, 'E': 2, 'R': 3, 'T': 4, 'Y': 5, 'U': 6, 'I': 7, 'O': 8, 'P': 9}
    left_set = {'1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T'}
    left_i, left_j = 1, 0
    right_i, right_j = 1, 9

    for word in line:
        word_i = keyboard_i[word]
        word_j = keyboard_j[word]
        left_flag_i = abs(left_i - word_i)
        left_flag_j = abs(left_j - word_j)
        left_flag = left_flag_i + left_flag_j

        right_flag_i = abs(right_i - word_i)
        right_flag_j =  abs(right_j - word_j)
        right_flag = right_flag_i + right_flag_j

        if left_flag > right_flag:
            answer.append(1)
            right_i, right_j = word_i, word_j

        elif left_flag < right_flag:
            answer.append(0)
            left_i, left_j = word_i, word_j

        else:
            if left_flag_j > right_flag_j:
                answer.append(1)
                right_i, right_j = word_i, word_j

            elif left_flag_j < right_flag_j:
                answer.append(0)
                left_i, left_j = word_i, word_j

            else:
                if word in left_set:
                    answer.append(0)
                    left_i, left_j = word_i, word_j
                else:
                    answer.append(1)
                    right_i, right_j = word_i, word_j



    return answer

print(solution("Q4OYPI"))