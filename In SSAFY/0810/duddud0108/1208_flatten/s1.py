import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    box_list = list(map(int, input().split()))

    max_index = min_index = 0
    for i in range(N+1):
        max_num = 0
        min_num = 100
        for j in range(len(box_list)):
            if max_num < box_list[j]:
                max_num = box_list[j]
                max_index = j
            if min_num > box_list[j]:
                min_num = box_list[j]
                min_index = j
        if i != N:
            box_list[min_index] += 1
            box_list[max_index] -= 1

    result = box_list[max_index] - box_list[min_index]

    print('#{0} {1}'.format(tc+1, result))