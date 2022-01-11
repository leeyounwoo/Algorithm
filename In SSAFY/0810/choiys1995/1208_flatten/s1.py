
import sys

sys.stdin = open('input.txt')

def find_minmax(boxes):#최대값, 최소값 찾는 함수

    tempmin = 1000
    tempmax = 0
    for i in boxes:
        if tempmin > i:
            tempmin = i
        if tempmax < i:
            tempmax = i

    return tempmin, tempmax

for T in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        max_box = min_box = boxes[0]
        min_box, max_box = find_minmax(boxes)
        ans = max_box - min_box

        if ans >= 2:# 1이하일 경우 서로 값만 바뀌고 차이는 변함없음
            flag_max = 1
            flag_min = 1
            for j in range(len(boxes)):# 최대값 박스에서 1을 빼서 최소값 박스에 줌
                if not flag_max and not flag_min:
                    break
                if flag_max and boxes[j] == max_box:
                    boxes[j] -= 1
                    flag_max = 0
                if flag_min and boxes[j] == min_box:
                    boxes[j] += 1
                    flag_min = 0
        else:# 1이하면 연산 그만하고 반복문 나오기
            break
    #평탄화 작업을 한 index가 작업 후에도 min, max란 보장이 없으므로 다시한번 연산
    else:
        max_box = min_box = boxes[0]
        min_box, max_box = find_minmax(boxes)
        ans = max_box - min_box
    print('#{} {}'.format(T, ans))