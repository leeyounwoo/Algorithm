import sys
sys.stdin = open('input.txt')
def two_num(num):
    for i in range(len(num)):
        two_total = 0
        if num[i] == 0:
            num[i] = 1
            for j in range(len(num)):
                two_total += two[j] * (2 ** (len(num) - 1 - j))
            two_lst.append(two_total)
            num[i] = 0
        elif num[i] == 1:
            num[i] = 0
            for j in range(len(num)):
                two_total += two[j] * (2 ** (len(num) - 1 - j))
            two_lst.append(two_total)
            num[i] = 1

def three_num(num):
    for i in range(len(num)):
        if num[i] == 0:
            num[i] = 1
            three_total = 0
            for j in range(len(num)):
                three_total += three[j] * (3 ** (len(num) - 1 - j))
            three_lst.append(three_total)
            num[i] = 0
        if num[i] == 0:
            num[i] = 2
            three_total = 0
            for j in range(len(num)):
                three_total += three[j] * (3 ** (len(num) - 1 - j))
            three_lst.append(three_total)
            num[i] = 0
        if num[i] == 1:
            num[i] = 0
            three_total = 0
            for j in range(len(num)):
                three_total += three[j] * (3 ** (len(num) - 1 - j))
            three_lst.append(three_total)
            num[i] = 1
        if num[i] == 1:
            num[i] = 2
            three_total = 0
            for j in range(len(num)):
                three_total += three[j] * (3 ** (len(num) - 1 - j))
            three_lst.append(three_total)
            num[i] = 1
        if num[i] == 2:
            num[i] = 0
            three_total = 0
            for j in range(len(num)):
                three_total += three[j] * (3 ** (len(num) - 1 - j))
            three_lst.append(three_total)
            num[i] = 2
        if num[i] == 2:
            num[i] = 1
            three_total = 0
            for j in range(len(num)):
                three_total += three[j] * (3 ** (len(num) - 1 - j))
            three_lst.append(three_total)
            num[i] = 2

T = int(input())
for tc in range(1, T+1):
    two = list(map(int, input()))
    three = list(map(int, input()))
    two_lst = []
    three_lst = []
    two_num(two)
    three_num(three)
    for i in range(len(two_lst)):
        for j in range(len(three_lst)):
            if two_lst[i] == three_lst[j]:
                result = two_lst[i]
    print('#{} {}'.format(tc, result))