import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cnt = int(input())
    triangle = [[1]] # 첫번째 줄을 만들어 줌
    for i in range(cnt-1):
        tmp = [1] # 기본으로 1을 맨 앞에 추가
        for j in range(len(triangle[i])-1):
            tmp.append(triangle[i][j] + triangle[i][j+1]) # 이전 줄의 j번째 j+1번째를 합한 값을 다음 줄에 추가
        tmp.append(1) # 마지막으로 닫는 1을 추가
        triangle.append(tmp) # 최종 삼각형에 줄을 추가

    print('#{0}'.format(tc))
    for line in triangle:
        print(' '.join(map(str, line)))
