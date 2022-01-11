import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    print('#{}'.format(tc+1))
    num = int(input())
    rect = [[1], [1, 1]]
    if num <= 2:
        for i in range(num):
            print(*rect[i])
    else:
        for i in range(2, num):
            temp = [1]
            for j in range(1, i):
                temp.append(rect[i-1][j-1] + rect[i-1][j])
            temp.append(1)
            rect.append(temp)

        for arr in rect:
            print(*arr)



