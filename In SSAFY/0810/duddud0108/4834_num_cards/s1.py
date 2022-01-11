import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    number_list = list(map(int, list(input())))

    counts = [0]*10
    for i in range(N):
        counts[number_list[i]] += 1

    max_count = 0
    number = 0
    for i in range(10):
        if counts[i] >= max_count:
            number = i
            max_count = counts[i]

    print('#{0} {1} {2}'.format(tc+1, number, max_count))


