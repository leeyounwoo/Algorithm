# 10개의 정수 입력받아 부분집합의 합이 0이되는것이 존재하는지 계산하는 함수
arr = [-1, 2, 5, 10, -7, 0, 8, 9, 4, 13]
n= len(arr)

for i in range(1 <<n):

    # 부분집합이 만들어지는 부분
    total = 0
    for j in range(n):
        if i & (1 << j):
            # 여기서 하고싶은 일 수행
            total += arr[j]
    if total == 0:
        print('0이 되는 경우가 있습니다!')
