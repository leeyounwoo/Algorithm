def my_func(pick, r):
    global cnt
 
    if r == N:
        cnt += 1
        return
 
    for c in range(N):
        if not col[c] and not dia1[r+c] and not dia2[r-c+(N-1)]:
            col[c], dia1[r+c], dia2[r-c + (N-1)] = 1, 1, 1
            my_func(pick+[c], r+1)
            col[c], dia1[r+c], dia2[r-c + (N-1)] = 0, 0, 0
 
 
for tc in range(1, int(input())+1):
    N = int(input())
    col = [0] * N
    dia1 = [0] * (2 * N - 1) 
    dia2 = [0] * (2 * N - 1) 
 
    cnt = 0
    my_func([], 0)
    print("#{} {}".format(tc, cnt))