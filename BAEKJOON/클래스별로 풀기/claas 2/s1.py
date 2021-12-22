import sys

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
check = [False for _ in range(n)]
numbers = [int(sys.stdin.readline()) for _ in range(n)]
ans = []
flag_no = False
for i in range(n):
    # print(f)
    index = numbers[i] - 1
    # index 보다 큰 값 중에 True 값이 있는지 확인
    flag_bigger = False
    max_true = -1
    for j in range(index+1, n):
        if check[j]:
            flag_bigger = True
            max_true = j
            break
    # 큰 값 중에 True가 있는 경우, 현재 값과 큰 값중에 False가 있으면 안됌
    if flag_bigger:
        for j in range(index+1, max_true):
            if not check[j]:
                flag_no = True
                break
    if flag_no:
        break
    if flag_bigger:
        ans.append('-')
    else:
        for j in range(index-1, -1, -1):
            if check[j]:
                ans += ['+'] * (index - j)
                break
        else:
            ans += ['+'] * (index+1)
        ans.append('-')
    check[index] = True

if flag_no:
    print("NO")
else:
    for i in range(len(ans)):
        print(ans[i])