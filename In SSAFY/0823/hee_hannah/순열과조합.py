def comb(n, picked, to_pick):
    if to_pick == 0:
        print(picked)
        return

    # 순열과 조합의 차이?
    # 조합은 이전에 뽑은 위치는 다시 쓰지 않음!
<<<<<<< HEAD
    for i in range(n):
=======
    smallest = 0 if not picked else picked[-1]
    for i in range(smallest, n):
>>>>>>> 548daa4abe5e97aacab0c6d163197eb688f08bf3
        if i not in picked:
            picked.append(i)
            perm(n, picked, to_pick - 1)
            picked.pop()

def perm(n, picked, to_pick):
    if to_pick == 0:
        # 실제 picked에는 해당 원소의 "인덱스"가 담겨있습니다.
        for idx in picked:  # idx: 실제 nums의 인덱스로 사용 가능
            print(nums[idx], end=" ")
        print()

    for i in range(n):
        if i not in picked:
            picked.append(i)
            perm(n, picked, to_pick - 1)
            picked.pop()


nums = [1, 2, 3]
<<<<<<< HEAD
perm(len(nums), [], 3)  # 순열
comb(len(nums), [], 2)  # 조합
=======
perm(len(nums), [], 3) # 순열
# comb(len(nums), [], 2) # 조합
>>>>>>> 5b9cc58c83f42366c32080b5e6748bd61bea6936
