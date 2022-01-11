import sys
sys.stdin = open('input.txt')

# 트럭 당 한 개의 컨테이너
# tru_c 넘는 conta_w는 운반 불가능
T = int(input())
for tc in range(1, T+1):
    conta, tru = map(int, input().split()) # 컨테이너 수, 트럭 수
    conta_w = list(map(int, input().split()))# 컨테이너 화물 무게
    tru_c = list(map(int, input().split())) # 트럭 적재용량

    # 화물 무게를 sort한 후에
    # 트럭 용량도 sort한 후에
    container = sorted(conta_w) # 1 3 5
    truck = sorted(tru_c)       # 3 8

    total_w = 0
    for i in range(min(conta, tru)): # 0 1
        if container[-1] > truck[-1] : # tru_c 넘는 conta_w는 운반 불가능
            container.pop()
        else:
            total_w += container.pop()
            truck.pop() # 트럭 당 한 개의 컨테이너


    print('#{} {}'.format(tc, total_w))