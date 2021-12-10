for T in range(int(input())):
    start, end = map(int, input().split())
    speed = 1
    ans = 0
    while True:
        print(start, end, speed, ans)
        ans += 2
        start += speed
        end -= speed
        if end - start == speed -1 or end - start == speed or end - start == speed + 1:
            ans += 1
            break
        speed += 1

    print(ans)