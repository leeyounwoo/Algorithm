import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    contain, truck = map(int, input().split())
    con_weight = list(map(int, input().split()))
    truck_weight = list(map(int, input().split()))
    con_weight.sort(reverse=True) # 컨테이너의 무게를 내림차순으로 정렬
    truck_weight.sort(reverse=True) # 트럭이 실을 수 있는 무게도 내림차순으로!
    total = 0

    for i in truck_weight:
        for j in con_weight:
            if i >= j: #만약 트럭이 실을 수 있는 양의 최대치라면
                total += j #토탈에 담고
                con_weight.remove(j) # 담은 애는 없애주기
                break
            elif i < min(con_weight): # 트럭이 남아잇는 화물들을 실을수 없다면
                continue # 넘기기

    print(total)

    # 추천문제 : 2806. N-Queen D3