# 고정비용 A, 가변 비용 B, 판매가격 C
a, b, c = map(int, input().split())
profit = c - b
if profit <= 0:
    print(-1)
else:
    cnt, rest = divmod(a, profit)
    print(cnt+1)