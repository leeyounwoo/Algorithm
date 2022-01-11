import sys
sys.stdin = open('input.txt')

def find(numbers):
    max_num = -1
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            num = numbers[i] * numbers[j]

            if num > max_num:
                num_s = str(num_s)
                for i in range(len(num_s) - 1):
                    if num_s[i] > num_s[i + 1]:
                        break
                else:
                    max_num = num
    return max_num

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, find(numbers)))
