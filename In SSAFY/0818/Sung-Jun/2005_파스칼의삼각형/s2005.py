import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    numbers = int(input())
    result = []
    befor_result = result[:]

    print('#{}'.format(tc+1))
    for test in range(numbers):
        if len(result) <= 1:
            result.append(1)
        else:
            befor_result = result[:]
            result.append(1)

            for num_list in range(len(result)):
                if num_list in [0, len(result) - 1]:
                    pass
                else:
                    result[num_list] = befor_result[num_list - 1] + befor_result[num_list]
        print(*result)