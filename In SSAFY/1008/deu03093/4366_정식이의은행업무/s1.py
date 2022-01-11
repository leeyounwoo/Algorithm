import sys
sys.stdin = open('input.txt')


def make_list_num_2(num_2):
    result = []
    for i in range(len(num_2)):
        start = num_2[:]
        if start[i] == 1:
            start[i] = 0
        elif start[i] == 0:
            start[i] = 1
        result.append(start)
    # print(result)
    return result


def make_list_num_3(num_3):
    result = []
    for i in range(len(num_3)):
        start = num_3[:]
        if start[i] == 0:
            start[i] = 1
            result.append(start)
            start = num_3[:]
            start[i] = 2
            result.append(start)
        elif start[i] == 1:
            start[i] = 0
            result.append(start)
            start = num_3[:]
            start[i] = 2
            result.append(start)
        elif start[i] == 2:
            start[i] = 0
            result.append(start)
            start = num_3[:]
            start[i] = 1
            result.append(start)
    # print(result)
    return result


def convert_2_to_10(candidate_2):
    result = []
    for i in range(len(candidate_2)):
        num_2 = candidate_2[i]
        num_2.reverse()
        temp = 1
        num_10 = 0
        for j in range(len(num_2)):
            num_10 += temp * num_2[j]
            temp *= 2
        result.append(num_10)
    return result


def convert_3_to_10(candidate_3):
    result = []
    for i in range(len(candidate_3)):
        num_3 = candidate_3[i]
        num_3.reverse()
        temp = 1
        num_10 = 0
        for j in range(len(num_3)):
            num_10 += temp * num_3[j]
            temp *= 3
        result.append(num_10)
    return result


for T in range(1, 1+int(input())):
    num_2 = list(map(int, list(input())))
    num_3 = list(map(int, list(input())))
    # print(num_2)
    # print(num_3)
    candidate_2 = make_list_num_2(num_2)
    candidate_3 = make_list_num_3(num_3)
    result_2 = convert_2_to_10(candidate_2)
    result_3 = convert_3_to_10(candidate_3)
    # print(result_2)
    # print(result_3)
    for i in range(len(result_2)):
        if result_2[i] in result_3:
            ans = result_2[i]
            break
    print('#{} {}'.format(T, ans))
