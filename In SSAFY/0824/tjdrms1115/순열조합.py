from itertools import combinations


def comb(n, picked, to_pick):
    if to_pick == 0:
        print(picked)
        return

    # 순열 조합 차이?
    # 조합은 한 번 지나간 위치는 다시 보지 않는다!

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            perm(n, picked, to_pick - 1)
            picked.pop()


def perm(n, picked, to_pick):
    if to_pick == 0:
        print(picked)
        return
    # 실제 picked에는 인덱스가 담겨있습니다.

    for i in range(n):
        if i not in picked:
            picked.append(i)
            perm(n, picked, to_pick - 1)
            picked.pop()


nums = [1, 2, 3]
perm(len(num), [], 3)  # 순열
comb(len(num), [], 2)  # 조합


