arr = [-1, 5, 10, 7, -5, 9, 2, 3, 0, 15]
n = len(arr)

for i in range(1 << n):

    # 부분집합이 만들어지는 부분
    total = 0
    for j in range(n):
        if i & (1 << j):
            #여기서 하고 싶은 일 수행
            total += arr[j]  # 10 -5 2
    if total == 0:
        print('0이 되는 경우가 있습니다!')

