import sys
sys.stdin = open('1005/woosteelz/5201_컨테이너/sample_input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    con_weight = list(map(int, input().split()))
    truck_weight = list(map(int, input().split()))

    temp = []

    con_weight.sort()
    truck_weight.sort()

    while con_weight:
        if truck_weight and con_weight[-1] <= truck_weight[-1]:
            temp.append(con_weight.pop(-1))
            truck_weight.pop(-1)
        else:
            con_weight.pop(-1)
    print(f"#{tc} {sum(temp)}")
