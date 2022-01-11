import sys
sys.stdin = open('input.txt')

def permutation(total):
    global staff, max_success

    if total <= max_success:
        return

    if len(staff) == N:
        max_success = max(max_success, total)
        return
    else:
        for i in range(N):
            if i not in staff:
                staff.append(i)
                permutation(total * (success[len(staff)-1][staff[-1]] / 100))
                staff.pop()


T = int(input())

for t in range(1, T+1):
    N = int(input())
    success = [list(map(int, input().split())) for _ in range(N)]
    staff = []

    max_success = 0
    permutation(1)

    print('#{} {:0.6f}'.format(t, round(max_success*100, 6)))