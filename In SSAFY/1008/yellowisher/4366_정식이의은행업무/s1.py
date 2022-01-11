T = int(input())
 
for tc in range(1, T+1):
    bi = list(map(int, input()))
    tri = list(map(int, input()))
    cand = []
    for i in range(1, len(bi)):
        temp = 2**(len(bi)-1)
        for j in range(1, len(bi)):
            if i == j:
                temp += ((bi[j]+1)%2)*2**(len(bi)-j-1)
            else:
                temp += (bi[j])*2**(len(bi)-j-1)
        cand.append(temp)
 
    for k in cand:
        check, cnt, p = k, 0, 1
        while check:
            if check%3 == tri[len(tri)-p]:
                cnt += 1
            p += 1
            check //= 3
        if cnt == len(tri)-1:
            print('#{} {}'.format(tc, k))
            break