import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    numbers_list = [2, 3, 5, 7, 11]

    for k in numbers_dict.keys():
        while N % k == 0:
            N //= k
            numbers_dict[k] += 1

    result = '#{} '.format(tc)
    for number in numbers_list:
        result += str(numbers_dict[number]) + ' '

    print(result)