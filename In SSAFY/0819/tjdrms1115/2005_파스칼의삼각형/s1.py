import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    # 파스칼의 삼각형을 저장할 리스트입니다.
    triangle = []
    for i in range(N):

        if i == 0:
            triangle.append([1])
        else:
            # 파스칼의 삼각형 공식에 따라 파스칼의 삼각형을 만들어갑니다.
            templist = []
            templist.append(1)
            for j in range(1, i):
                templist.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            templist.append(1)
            # 한 줄이 완성될 때마다 저장합니다.
            triangle.append(templist)

    # 완성된 삼각형을 출력합니다.
    print('#{} '.format(tc))
    for i in triangle:
        s = map(str, i)
        print(' '.join(s))

