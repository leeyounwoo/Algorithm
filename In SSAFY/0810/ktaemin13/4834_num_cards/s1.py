import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    count = input()
    numbers = input()
    numbers = list(map(int, numbers))

    cnt = 0
    result = 0
    for number in numbers:
        if numbers.count(number) > cnt:
            cnt = numbers.count(number)
            result = number


    print('#{0} {1} {2}'.format(tc+1,number,cnt))