arr = [1, 2, 3, 4]
n = len(arr)
# 0001
# 0010
# 0100
# 10000011
# 0110
# 1100
# 0101
# 1001
# ...~
# 1111
total = 0
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            total += arr[j]
    if total == 0:
        print('0이 되는 경우가 있습니다!')