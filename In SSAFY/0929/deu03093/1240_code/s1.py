import sys
sys.stdin = open('input.txt')

def find_code_i(codes):
    code_i_list = []
    last_index = 0
    for i in range(len(codes)):
        for j in range(len(codes[i])-1, -1, -1):
            if codes[i][j] == '1':
                last_index = j
                code_i_list.append(i)
                break
    return (code_i_list, last_index)

for T in range(1, 1+int(input())):
    N, M = map(int, input().split())
    codes = [list(input()) for _ in range(N)]
    code_i_list, last_index = find_code_i(codes)
    first_index = last_index - 55
    for i in code_i_list:
        goal = []
        for j in range(last_index, last_index-57, -7):
            if j < first_index:
                break
            temp = codes[i][j-6:j+1]
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
        odd_sum = goal[0] + goal[2] + goal[4] + goal[6]
        even_sum = goal[1] + goal[3] + goal[5]
        flag_num = goal[7]
        r = ((odd_sum * 3) + even_sum + flag_num) % 10
        if not r:
            ans = sum(goal)
            break
    else:
        ans = 0
    print('#{} {}'.format(T, ans))
