import sys

sys.stdin = open('input.txt')

def my_max(numbers) :
    max_num = 0
    for num in numbers :
        if num > max_num :
            max_num = num
    return max_num

def my_min(numbers) :
    min_num = 100
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


for t in range(1, 11) :
    N = int(input())
    box = list(map(int, input().split()))

    for _ in range(N) :
        max_num = my_max(box)
        min_num = my_min(box)

        if max_num - min_num in [0, 1] :
            print(f'#{t} {max_num - min_num}')
            break
        else :
            box[box.index(max_num)] -= 1
            box[box.index(min_num)] += 1

    max_num = my_max(box)
    min_num = my_min(box)

    print(f'#{t} {max_num-min_num}')
