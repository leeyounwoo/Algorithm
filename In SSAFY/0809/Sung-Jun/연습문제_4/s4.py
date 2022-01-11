import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    numbers = input()
    check_list = [0]*10

    for number in numbers:
        check_list[int(number)] += 1

    triplet = 0
    run = 0
    for i in range(len(check_list)):
        if check_list[i] >= 3:
            check_list[i] -= 3
            triplet += 1
            continue
        elif check_list[i] >= 1 and check_list[i+1] >= 1 and check_list[i+2] >= 1 :
            check_list[i] -= 1
            check_list[i+1] -= 1
            check_list[i+2] -= 1
            run += 1
            continue
    if triplet >= 2 or run >= 2:
        print('baby-gin이 아니다.')
    elif triplet + run == 2 :
        print('baby-gin이다.')
    else:
        print('baby-gin이 아니다.')



