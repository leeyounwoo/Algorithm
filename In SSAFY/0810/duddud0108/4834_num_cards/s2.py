import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    number_list = list(map(int, list(input())))+[10]
    number_list.sort()

    number = number_list[0]
    count = 1
    max_count = 0
    for i in range(1, N+1):
        if number == number_list[i]:
            count += 1
        else:
            if count >= max_count:
                max_count = count
                max_number = number
            number = number_list[i]
            count = 1

    print('#{0} {1} {2}'.format(tc + 1, max_number, max_count))
