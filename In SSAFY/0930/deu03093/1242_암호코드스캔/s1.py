import sys
sys.stdin = open('input.txt')

def find_code_i(codes):
    code_i_j_list = []
    for i in range(len(codes)):
        flag = False
        for j in range(len(codes[i])-1, -1, -1):
            # '0'이 아닌 값을 만나지 못했을 때
            if not flag:
                if codes[i][j] != '0':
                    flag = True
                    code_i_j_list.append((i, j))
            else:
                if codes[i][j] == '0':
                    flag = False
    return code_i_j_list


def FindRowLastIndex(row):
    for i in range(len(row)-1, -1, -1):
        if row[i] != '0':
            return i


dict_16_to_10 = {
    '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', '0': '0000',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
for T in range(1, 1+int(input())):
    N, M = map(int, input().split())
    codes = [list(input()) for _ in range(N)]
    code_i_j_list = find_code_i(codes)
    print(code_i_j_list)
    for i, last_index in code_i_j_list:
        first_index = last_index - 14
        # print(first_index)
        # print(codes[i][first_index])
        row = ''
        temp = ''
        for r in range(first_index, last_index+1):
            temp += codes[i][r]
            row += dict_16_to_10[codes[i][r]]
        row_last_index = FindRowLastIndex(row)
        # print(row)
        row = row[row_last_index-55:row_last_index+1]
        print(row)
        goal = []
        for j in range(55, -2, -7):
            if j < 0:
                break
            temp = row[j-6:j+1]
            number = -1
            # 5번째 문자가 '0'인 경우 ==> 0, 1, 3, 5
            if temp[5] == '0':
                # 4번째 문자가 '0'인 경우 ==> 1, 5
                if temp[4] == '0':
                    # 3번째 문자가 '1'인 경우 ==> 1
                    if temp[3] == '1':
                        number = 1
                    else:
                        number = 5
                else:
                    # 1번째 문자가 '1'인 경우 ==> 3
                    if temp[1] == '1':
                        number = 3
                    else:
                        number = 0
            # 2, 4, 6, 7, 8, 9
            else:
                if temp[1] == '0':
                    if temp[2] == '1':
                        number = 2
                    else:
                        number = 9
                else:
                    if temp[2] == '1':
                        if temp[3] == '1':
                            number = 7
                        else:
                            number = 8
                    else:
                        if temp[3] == '1':
                            number = 6
                        else:
                            number = 4
            goal.append(number)
        goal.reverse()
        # print(goal)
        odd_sum = goal[0] + goal[2] + goal[4] + goal[6]
        even_sum = goal[1] + goal[3] + goal[5]
        flag_num = goal[7]
        r = ((odd_sum * 3) + even_sum + flag_num) % 10
        if not r:
            ans = sum(goal)
    #         break
    # else:
    #     ans = 0
        print('#{} {}'.format(T, ans))
