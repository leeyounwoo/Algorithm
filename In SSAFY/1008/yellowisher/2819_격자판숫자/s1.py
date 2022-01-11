def check(r, c, k, tmp, N):
    if r<0 or r>=N or c<0 or c>=N:
        return
    if k == 7:
        result.add(tmp)
    else:
        tmp += arr[r][c]
        check(r+1, c, k+1, tmp, N)
        check(r, c+1, k+1, tmp, N)
        check(r-1, c, k+1, tmp, N)
        check(r, c-1, k+1, tmp, N)

T = int(input())
 
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    result = set()
    tmp = ''
    for r in range(4):
        for c in range(4):
            k = 0
            check(r, c, k, tmp, 4)
    ans = len(result)
     
    print(f'#{tc} {ans}')