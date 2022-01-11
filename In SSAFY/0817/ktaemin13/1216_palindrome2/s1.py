import sys
sys.stdin = open('input.txt')

for tc in range(10):

    T = int(input())
    arr = [input() for _ in range(100)]

    result = ''
    cnt = 0
    # mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #

    while cnt < 100:
        for i in range(99):
            for j in range(1, 100):
                if len(arr[cnt][i:i+j]) >= len(result) and arr[cnt][i:i+j] == arr[cnt][i+j-101:i-101:-1]:
                    result = arr[cnt][i:i+j]
        cnt += 1

    cnt = 0
    new_list = list(map(list, zip(*arr)))
    while cnt < 100:
        for i in range(99):
            for j in range(1, 100):
                if len(new_list[cnt][i:i+j]) >= len(result) and new_list[cnt][i:i+j] == new_list[cnt][i+j-101:i-101:-1]:
                    result = new_list[cnt][i:i+j]
        cnt += 1
    print('#{0} {1}'.format(tc+1, len(result)))