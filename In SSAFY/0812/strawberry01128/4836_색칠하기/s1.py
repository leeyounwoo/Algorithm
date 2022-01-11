import sys
sys.stdin = open('input.txt')

# 입력 받는 과정
Test = int(input())
for test_case in range(1,Test+1):
    square = int(input())
    result = []
    answer = 0
    pan = [[0]*10 for _ in range(10)]
    for color_box in range(square):
        box_info = list(map(int, input().split()))
        result.append(box_info)

    print(result)

# 색칠하는 방법, 다 0으로 넣었을때 (2,2)~(4,4) 까지 색깔정보 1넣을꺼임
# [0][0]-> x1 , [0][1]->y1 [0][3] -> x2 [0][4]->y2  [0][5] ->색정보
    for i in range(len(result)):
        # pan[result[i][0]][result[i][1]] = result[i][4]
        # X 축 칠하기
        for j in range(0,result[i][2]-result[i][0]+1):#->()안은 2,3
            # y 축 칠하기
            for p in range(0,result[i][3]-result[i][1]+1):
                if pan[result[i][0] + j][result[i][1] + p] != result[i][4] and pan[result[i][0] + j][result[i][1] + p] != 0:
                    answer += 1

                else:
                    pan[result[i][0] + j][result[i][1] + p] = result[i][4]
    print('#{} {}'.format(test_case,answer))