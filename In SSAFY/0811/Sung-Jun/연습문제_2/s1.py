arr = [1, 5, 10, 7, -5, 9, 2, 3, 0, 15]

len_num = len(arr)
result = 0

for i in range(1 << len_num):
    total = 0
    for j in range(len_num):
        if i & (1 << j):
            total += arr[j]
    if total == 0:
        result += 1

if result >= 1 :
    print('0이 되는 경우가 있습니다.')
