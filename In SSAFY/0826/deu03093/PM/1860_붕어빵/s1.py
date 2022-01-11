import sys
sys.stdin = open('input.txt')

for T in range(1, 1+int(input())):
    peoples, time, bread = map(int, input().split())
    guests_time = list(map(int, input().split()))

    serve_dict = {}
    for i in range(len(guests_time)):
        if guests_time[i] in serve_dict:
            serve_dict[guests_time[i]] += 1
        else:
            serve_dict[guests_time[i]] = 1
    serve_times = list(serve_dict.keys())
    serve_times.sort()
    last_guest = serve_times[-1]
    if serve_times[0] == 0:
        ans = "Impossible"
    else:
        ans = "Possible"
        bread_total = 0
        for i in range(1, last_guest+1):
            if i % time == 0:
                bread_total += bread
            if i in serve_times:
                bread_total -= serve_dict[i]
            if bread_total < 0:
                ans = 'Impossible'
                break

    print('#{} {}'.format(T, ans))


