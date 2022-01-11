import sys
sys.stdin = open('input.txt')

def pizza():
    fire_pit = []  # 피자 돌리기
    fire_index = []  # 피자 리스트 돌리기
    cnt = 0
    for i in range(N):
        fire_pit.append(cheese_list.pop(0))  # 오븐에 피자 채우기
        fire_index.append(cheese_index.pop(0))  # 피자 인덱스 채우기
    while len(fire_pit) != 1:  #  오븐에 피자가 1개 남았다면
        while fire_pit[-1] != 0:  # 치즈가 다 녹을 때 까지
            fire_pit.insert(0, fire_pit.pop(0)//2)  # 치즈 반으로 녹이기
            fire_pit.append(fire_pit.pop(0))  #  녹인 피자 맨 뒤로 보내기
            fire_index.append(fire_index.pop(0))  # 피자의 index도 맨 뒤로 보내기
        fire_pit.pop()  # 치즈가 다 녹았으면(==0) 피자 꺼내기
        fire_index.pop()  # 그 피자의 index도 꺼내기
        if N+cnt >= M:
            continue
        else:
            fire_pit.insert(0, cheese_list.pop(0))
            fire_index.insert(0, cheese_index.pop(0))
            cnt += 1
    return  print('#{} {}'.format(tc+1, *fire_index))



T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    cheese_list = list(map(int, input().split()))
    cheese_index = []
    for i in range(1, M+1):
        cheese_index.append(i)
    pizza()
