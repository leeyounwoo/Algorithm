import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    triangle = []
    for i in range(N):

        if i == 0:
            triangle.append([1])
        else:
            templist = []
            templist.append(1)
            for j in range(1, i):
                templist.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            templist.append(1)

            triangle.append(templist)

    print('#{} '.format(tc))
    for i in triangle:
        s = map(str, i)
        print(' '.join(s))

