import sys
sys.stdin = open('input.txt')


for T in range(1, 1+int(input())):
    arr = list(map(int, input().split()))
    # 목적지
    goal = arr[0] - 1
    # 배터리 충전 용량
    batterys = arr[1:]
    now = 0
    # 현재 정류장에서 갈 수 있는 가장 먼 정류장
    can_go = now + batterys[0]
    cnt = 0
    # 갈 수 있는 정류장이 목적지보다 멀거나 같은 경우에 반복문 종료
    while can_go < goal:
        # 현재 배터리량으로 갈 수 있는 정류장들에서 갈 수 있는 가장 먼 정류장들
        can_list = []
        # 각 정류장들의 번호
        can_index = []
        # 현재 정류장에서 갈 수 있는 정류장들
        for i in range(now+1, can_go+1):
            can_list.append(i+batterys[i])
            can_index.append(i)
        # 갈 수 있는 정류장에서 갈 수 있는 가장 먼 정류장을 선택
        can_go = max(can_list)
        # 현재 정류장 번호를 선택한 정류장으로 갱신
        now = can_index[can_list.index(can_go)]
        cnt += 1

    print('#{} {}'.format(T, cnt))
