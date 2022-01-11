import sys
sys.stdin = open('input.txt')

for tc in range(10):
    dump_count = int(input())
    dump_numbers = list(map(int, input().split()))

    i = 0

    while i <= dump_count:
        i += 1
        max, min = dump_numbers[0], dump_numbers[0]
        for number in dump_numbers:
            if number > max:
                max = number
            if number < min:
                min = number

        dump_numbers[dump_numbers.index((max))] = max-1
        dump_numbers[dump_numbers.index((min))] = min+1

    print('#{0} {1}'.format(tc+1,max-min))