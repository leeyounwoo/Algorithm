arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]

total = [[0]*5 for _ in range(5)]
delta = [(-1, 0), (1,0), (0, -1), (0,1)]

for i in range(len(arr)):
    for j in range(len(arr[i])):

        for di, dj in delta:
            # 만약 이웃한 요소가 배열의 범위를 벗어날 경우, 이웃한 요소가 아닌 자기 자신을 temp에 저장
            # (temp가 자기 자신이면 차이가 없으므로 무시해도 됨)

            if i+di not in range(5) or j+dj not in range(5):
                di = 0
                dj = 0

            temp = arr[i+di][j+dj]

            total[i][j] += abs(arr[i][j] - temp)

print(total)
