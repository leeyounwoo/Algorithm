import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    list_num = list(map(int, input().split()))
    find_page = [list_num[num] for num in range(1,len(list_num))]


    result = []
    for page in find_page:
        count = 0
        start = 1
        end = list_num[0]
        while start < end:
            count += 1
            middle = (start + end) // 2
            if middle == page:
                break
            elif middle < page:
                start = middle + 1
            else:
                end = middle - 1

        if start <= end:
            result.append(count)
        else:
            result.append(-1)

    if result[0] < result[1]:
        winner = 'A'
    elif result[0] > result[1]:
        winner = 'B'
    else:
        winner = 0
    print('#{} {}'.format(tc+1, winner))