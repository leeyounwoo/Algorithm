import sys
sys.stdin = open('input.txt')

from collections import deque

for T in range(1, 1+int(input())):
    fire_size, pizza_count = map(int, input().split())
    pizza = deque(list(map(int, input().split())))
    fire = deque()
    order = deque()
    count = 0
    for i in range(fire_size):
        # print(pizza.popleft())
        fire.append(pizza.popleft())
        order.append(count)
        count += 1

    check = [i for i in range(pizza_count)]
    while len(check) > 1:
        temp = fire.popleft()
        idx = order.popleft()
        temp //= 2
        if temp == 0:
            check.remove(idx)
            if pizza:
                fire.append(pizza.popleft())
                order.append(count)
                count += 1
        else:
            fire.append(temp)
            order.append(idx)

    print('#{} {}'.format(T, check[0] + 1))