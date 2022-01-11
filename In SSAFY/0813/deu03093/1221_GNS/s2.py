for T in range(1, int(input()) + 1):
    bus_count = int(input())
    stops_max = []
    stops_min = []
    for _ in range(bus_count):
        min_stop, max_stop = map(int, input().split())
        stops_max.append(max_stop)
        stops_min.append(min_stop)

    stop_count = int(input())
    stops = []
    for _ in range(stop_count):
        stops.append(int(input()))

    ans = [0] * (5001)
    for bus in range(bus_count):
        for stop in range(stops_min[bus], stops_max[bus] + 1):

            ans[stop] += 1
    print('#{}'.format(T), end=' ')
    for i in stops:
        print(ans[i], end=' ')
    print()