T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    blocks = list(map(int, input().split()))

    result = 0

    for i in range(len(blocks)):
        temp_max = 0

        for j in range(i + 1, len(blocks)):
            if blocks[i] > blocks[j]:
                temp_max += 1

        if temp_max > result:
            result = temp_max

    print(f'#{tc} {result}')