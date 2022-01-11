import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    answer = []

    while numbers:
        max_num = numbers[0]
        min_num = numbers[0]

        for i in range(len(numbers)):
            if max_num < numbers[i]:
                max_num = numbers[i]

        for i in range(len(numbers)):
            if min_num > numbers[i]:
                min_num = numbers[i]

        answer.append(max_num)
        numbers.remove(max_num)

        answer.append(min_num)
        numbers.remove(min_num)

    answer = answer[:10]
    result = ''
    for x in answer:
        result += str(x) + ' '

    print('#{0} {1}'.format(tc, result))