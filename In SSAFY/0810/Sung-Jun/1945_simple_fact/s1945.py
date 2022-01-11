import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    numbers = int(input())
    check_list = [2, 3, 5, 7, 11]
    result = [0]

    print('#{0}'.format(tc+1), end=' ')
    for num in check_list:
        count = 0
        while True:
            if numbers % num == 0:
                numbers = int(numbers/num)
                count += 1
            else:
                result[0] = count
                break
        print(result[0], end=' ')
    print()

