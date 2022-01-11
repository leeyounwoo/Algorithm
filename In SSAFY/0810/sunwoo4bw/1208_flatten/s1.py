import sys
sys.stdin = open('input.txt')

T = 10 # 총 10개의 테스트케이스

for tc in range(1, T+1):
    num = int(input())  # 덤프 횟수
    box_arr = list(map(int, input().split()))  # [42, 68, 35, 1, 70, ...]

    for i in range(num+1):  # 0부터 num+1 까지-> num번째 flatten 이후의 max, min값
        max_h = 0
        min_h = 101       # 모든 위치에서 상자의 높이는 1이상 100이하
        for box in box_arr:
            if box > max_h :
                max_h = box
            if box < min_h :
                min_h = box
        box_arr[box_arr.index(max_h)] -= 1
        box_arr[box_arr.index(min_h)] += 1

    print('#{} {}'.format(tc, max_h - min_h))