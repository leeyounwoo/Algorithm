import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    bin_str = input()
    tri_str = input()

    bin_candidate = []
    for i in range(len(bin_str)):
        temp = ''
        if bin_str[i] == '0':
            temp = '1'
        else:
            temp = '0'
        temp = int(bin_str[0:i] + temp + bin_str[i + 1:], 2)
        bin_candidate.append(temp)

    tri_candidate = []
    case_set = [('1', '2'), ('0', '2'), ('0', '1')]
    for i in range(len(tri_str)):
        templist = []
        if tri_str[i] == '0':
            templist = case_set[0]
        elif tri_str[i] == '1':
            templist = case_set[1]
        else:
            templist = case_set[2]
        for c in templist:
            temp = int(tri_str[0:i] + c + tri_str[i + 1:], 3)
            tri_candidate.append(temp)

    result = 0
    for bin_num in bin_candidate:
        if bin_num in tri_candidate:
            result = bin_num
            break

    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')