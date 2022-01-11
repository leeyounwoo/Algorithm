import sys
sys.stdin = open('input.txt')


def bung_a_bbang():
    bread_count = 0
    result = 'Possible'
    for i in arrive_list:  # 붕어빵을 굽기 전에 손님이 먼저 도착한다면 Impossible
        if i < time:
            return 'Impossible'
    while arrive_list:  # 손님이 time에 도착했을 때, 붕어빵이 이미 1개 이상 만들어져 있어야 한다.
         for j in range(max(arrive_list) + 1):  # 붕어빵 굽기
             if j > 0 and j % time == 0:  # time이 됐으면
                 bread_count += bread  # bread 만큼 추가
             if j == arrive_list[0]:  # 손님 도착
                 if bread_count > 0:
                     bread_count = bread_count -1  # 빵 하나 주고
                     arrive_list.pop(0)  # 손님 내보내기
                 else:
                     return 'Impossible'
    if bread_count >= 0:  # 붕어빵 남아있으면
        return result     # Possible
    else:
        return 'Impossible'  # 아니라면 Impossible


T = int(input())
for tc in range(T):
    guest, time, bread = map(int, input().split())
    arrive_list = sorted(list(map(int, input().split())))
    print('#{} {}'.format(tc + 1, bung_a_bbang()))