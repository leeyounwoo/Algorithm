import sys
sys.stdin = open('1005/woosteelz/5202_화물도크/sample_input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    form = [tuple(map(int, input().split())) for _ in range(N)]

    form.sort(key=lambda x: x[1])
    cnt = 1
    prev = form.pop(0)
    for f in form:
        if f[0] < prev[1]:
            continue
        else:
            prev = f
            cnt += 1

    print(f"#{tc} {cnt}")
