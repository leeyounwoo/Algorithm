import sys

# sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
cnt = {}
for num in list_n:
    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1

m = int(sys.stdin.readline())
list_m = list(map(int, sys.stdin.readline().split()))

ans = []
for i in range(m):
    if list_m[i] not in cnt:
        ans.append(str(0))
    else:
        ans.append(str(cnt[list_m[i]]))
print(' '.join(ans))