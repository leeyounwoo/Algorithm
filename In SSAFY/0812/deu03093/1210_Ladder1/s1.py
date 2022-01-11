import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    t = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    start_j = arr[99].index(2)

    for i in range(98, 0, -1):
        # 오른쪽으로 갔다가 다시 왼쪽으로 오지 않게 하기 위한 변수
        flag = 1
        while start_j + 1 <= 99 and arr[i][start_j + 1]:
            start_j += 1
            flag = 0

        # 위의 while문이 실행하지 않을 때만 실행한다는 뜻
        if flag:
            while 0 <= start_j - 1 and arr[i][start_j - 1]:
                start_j -= 1

    print('#{} {}'.format(T, start_j))