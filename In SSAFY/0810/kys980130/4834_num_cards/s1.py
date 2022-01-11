N = int(input())
for tc in range(N):
    M = int(input())
    cards = list(map(str, input()))
    check = [0] * 10
    for i in range(M):
        cards[i] = int(cards[i])
        check[cards[i]] += 1
    count = max(check)
    max_num = []
    for j in range(10):
        if count == check[j]:
            max_num.append(j)
    print(f'#{tc+1} {max(max_num)} {count}')
