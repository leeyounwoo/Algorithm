import sys

sys.stdin = open('input.txt')

for t in range(1, 11) :
    N = int(input())
    high = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2) :
        temp = []
        temp.append(high[i-2])
        temp.append(high[i-1])
        temp.append(high[i])
        temp.append(high[i+1])
        temp.append(high[i+2])

        cnt = len(temp)-1
        while cnt :
            for j in range(cnt) :
                if temp[j] > temp[j+1] :
                    temp[j], temp[j+1] = temp[j+1], temp[j]
            cnt -= 1

        if temp[-1] == high[i] :
            result += temp[-1] - temp[-2]

    print(f'#{t} {result}')