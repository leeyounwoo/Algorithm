for T in range(int(input())):
    start, end = map(int, input().split())
    speed = 1
    ans = 0
    if end - start == 1:
        ans = 1
    elif end - start == 2:
        ans = 2
    elif 3 <= end - start <= 4:
        ans = 3
    elif
