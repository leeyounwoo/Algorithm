import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(T):
    len_num = int(input())
    numbers = list(map(int, input().split()))

    result = 0
    for i in range(len_num-1):
        if i in [0, 1, len_num-2, len_num-1]:
            pass
        else:
            for j in range(1,numbers[i]+1):
                if numbers[i-2] < j and numbers[i-1] < j:
                    if numbers[i+1] < j and numbers[i+2] < j:
                        result += 1

    print('#{0} {1}' .format(tc+1, result))