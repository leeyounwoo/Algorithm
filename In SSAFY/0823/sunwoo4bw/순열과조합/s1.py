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
            perm(n, picked, to_pick - 1)
            picked.pop()


def perm(n, picked, to_pick):
    if to_pick == 0:
        # 실제 picked에는 해당 원소의 "인덱스"가 담겨있습니다.
        for idx in picked : #iox:실제 nums의 인덱스로 사용 가능
            print(nums[idx], end= ' ')
        print()
        return

    for i in range(n):
        if i not in picked:
            picked.append(i)
            perm(n, picked, to_pick - 1)
            picked.pop()

nums = [1, 2, 3]
perm(len(nums), [], 3)
comb(len(nums), [], 2)