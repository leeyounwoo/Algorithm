import sys
sys.stdin = open('input.txt')
#from itertools import combinations
#구글 적극 참고

def search(cnt, idx, start):
    if cnt == N // 2:
        flavor(0)
        return
    else:
        for i in range(start, N):
            fi[idx] = i
            search(cnt + 1, idx + 1, i + 1)
    return


def flavor(c):
    global min_tmp
    fi_sum = 0
    se_sum = 0

    for s in range(N):
        if s not in fi:
            se[c] = s
            c += 1

    for i in range(N // 2):
        for j in range(N // 2):
            if i != j:
                fi_sum += mat[fi[i]][fi[j]]
                se_sum += mat[se[i]][se[j]]

    if abs(fi_sum - se_sum) < min_tmp:
        min_tmp = abs(fi_sum - se_sum)
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    fi = [0]*(N // 2)
    se = [0]*(N // 2)

    min_tmp = 99999
    search(0, 0, 0)


    print('#{} {}'.format(tc, min_tmp))