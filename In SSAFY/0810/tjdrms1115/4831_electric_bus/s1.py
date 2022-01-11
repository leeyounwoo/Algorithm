import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    K, N, M = list(map(int, input().split()))
    batterylist = list(map(int, input().split()))
    batterypos = [0 for i in range(N + 1)]
    for i in batterylist:
        batterypos[i] += 1

    pos = 0  # current station number
    comebycount = 0  # count for number of station that the bus come by

    chksuccess = 1  # check parameter whether bus can go to end or not
    while (True):
        if pos + K >= N:
            break
        tmpchk = 0
        for i in range(K, 0, -1):
            if batterypos[pos + i] >= 1:
                pos = pos + i
                comebycount += 1
                tmpchk = 1
                break
        if tmpchk == 0:
            chksuccess = 0
            comebycount = 0
            break

    answer.append(comebycount)

for tc in range(1, T + 1):
    print('#{0} {1}'.format(tc, answer[tc-1]))

