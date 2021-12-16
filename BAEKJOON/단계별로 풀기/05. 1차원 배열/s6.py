n = int(input())
for _ in range(n):
    score = 0
    ans = 0
    a = input()
    for i in range(len(a)):
        if a[i] == 'O':
            score += 1
            ans += score
        else:
            score = 0
    print(ans)