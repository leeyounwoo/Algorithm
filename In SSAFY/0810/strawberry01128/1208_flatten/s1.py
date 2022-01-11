# import sys
# sys.stdin = open('input.txt')
# for test in range(1,11):
#     Dump = int(input())
#     box = list(map(int, input().split()))
#
#     for test_case in range(Dump):
#         box.sort()
#         if  not max(box) == min(box):
#             box[99] = box[99]-1
#             box[0] = box[0] +1
#     print(f'#{test} {max(box)-min(box)}')


# 교수님의 풀이법
import sys
sys.stdin = open('input.txt')

def find_max_min_box(boxes):
    max_height = 0
    max_idx = 0
    min_height = 987654321
    min_idx = 0

    for i in range(len(boxes)):
        height = boxes[i]
        if height > max_height :
            max_height = height
            max_idx = i
        if height < min_height :
            min_height = height
            min_idx = i
    return max_idx, min_idx

T = 10
for tc in range(1, 1+T):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):

        # 1. 가장 높이가 높은 박스 찾기
        # 2. 가장 높이가 낮은 박스 찾기
        max_idx, min_idx = find_max_min_box(boxes)
        # 3. 찾은 인덱스를 이용하여
        # 최고 높이 박스 -1
        # 최저 높이 박스 +1
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    max_idx, min_idx = find_max_min_box(boxes)
    result = boxes[max_idx] - boxes[min_idx]
    print('#{} {}'.format(tc, result))



