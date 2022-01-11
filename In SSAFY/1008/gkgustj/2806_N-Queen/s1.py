import sys
sys.stdin = open('input.txt')

def find_next(i):
    global answer

    if i == N:
        answer += 1
        return

    for j in range(N):
        if (j in col) or (i-j in l_to_r) or (i+j in r_to_l):
            continue

        col.add(j)
        l_to_r.add(i-j)
        r_to_l.add(i+j)

        find_next(i+1)

        col.remove(j)
        l_to_r.remove(i-j)
        r_to_l.remove(i+j)

            

T = int(input())

for t in range(1, T+1):
    N = int(input())

    answer = 0

    col = set()
    l_to_r = set()
    r_to_l = set()

    find_next(0)

    print('#{} {}'.format(t, answer))