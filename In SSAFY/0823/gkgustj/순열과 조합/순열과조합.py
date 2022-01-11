def comb(n, picked, to_pick):
    if to_pick == 0:
        print(picked)
        return

    # 순열과 조합의 차이?
    # 조합은 이전에 뽑은 위치는 다시 쓰지 않음!

    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            comb(n, picked, to_pick - 1)
            picked.pop()


def perm(n, picked, to_pick):
    if to_pick == 0:
        print(picked)
        return

    for i in range(n):
        if i not in picked:
            picked.append(i)
            perm(n, picked, to_pick - 1)
            picked.pop()

nums = [1, 2, 3]
perm(len(nums), [], 3) # 순열
print('-')
comb(len(nums), [], 2) # 조합