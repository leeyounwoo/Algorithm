def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n - 1) + paper(n - 2) * 2


TC = int(input())
for tc in range(TC):
    num = int(input()) // 10
    print(f"#{tc + 1} {paper(num)}")