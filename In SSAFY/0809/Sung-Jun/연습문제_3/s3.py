import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(T):
    len_num = int(input())
    numbers = list(map(int, input().split()))

    max_drop = []
    for number in range(len_num-1):
        drop_num = 0
        for j in range(number+1,len_num):
            if numbers[number] > numbers[j]:
                drop_num += 1
        max_drop.append(drop_num)

    result = []
    print(max_drop)
    for max in max_drop:
        if result == []:
            result.append(max)
        else:
            if result[0] < max:
                result[0] = max
    print(result[0])