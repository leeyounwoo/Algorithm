import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # [피자 번호 + 1, 피자 치즈 양]
    pizza = list(enumerate(list(map(int, input().split())), 1))
    oven = []

    # print(pizza)

    # 오븐 용량만큼 피자 넣고
    for _ in range(N):
        oven.append(pizza.pop(0))

    # 오븐에 피자 1개 남을때 까지 반복
    while len(oven) > 1:
        # 오븐에 자리가 남아있는데 피자가 있다면 넣기
        if len(oven) < N and pizza:
            oven.append(pizza.pop(0))

        # 오븐에서 피자 꺼내보기
        pizzaidx, cheese = oven.pop(0)

        # 치즈 양이 0 이라면 피자 제거 치즈가 남아있다면 뒤에 추가해준다.
        if cheese // 2 != 0:
            oven.append((pizzaidx, cheese // 2))

    # print(oven.pop(0))
    print('#{} {}'.format(tc, oven.pop(0)[0]))