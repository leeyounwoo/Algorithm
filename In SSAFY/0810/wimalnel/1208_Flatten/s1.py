import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

for tc in range(1, 11):  # 테케 10개 루프 돕니다~
    dump = int(input()) # 덤프 수
    box_list = list(map(int, input().split())) #박스 높이
    while dump:  # 덤프가 반복되는 동안은 계속해서 평활화 작업을 한다.
                  # while문은 반복의 수가 정해지지 않을때 사용하면 꿀이다!
        box_high = box_list[box_list.index(max(box_list))]
        box_high = box_high-1          #최대 위치의 값을 1개 감소
        box_low = box_list[box_list.index(min(box_list))]
        box_low = box_low + 1           #최소 위치의 값을 1개 증가
        dump = dump-1   #덤프 루프하나 돌 때 하나씩 감소

    result = box_high - box_low

    print("#{} {}".format(tc, result))  #결과 값 출력
##실패임당 ㅎㅎ
