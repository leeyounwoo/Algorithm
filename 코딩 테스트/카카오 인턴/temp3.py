def recusion(prev, intensity, start_gate):
    global ans_distance, ans_top
    for next in graphs[prev]:
        # 이번에 intensitiy가 더 길면 갱신
        if graphs[prev][next] > intensity:
            next_intensity = graphs[prev][next]
        else:
            next_intensity = intensity

        if next_intensity > ans_distance:
            continue

        # 산봉우리
        if next in summits1:
            if next_intensity < ans_distance:
                ans_top = next
                ans_distance = next_intensity
            if next_intensity == ans_distance and next < ans_top:
                ans_top = next
                ans_distance = next_intensity


        # 출입구라면
        elif next in gates1:
            continue

        # 쉼터
        else:
            recusion(next, next_intensity, start_gate)



ans_top = -1
ans_distance = 10000001
graphs = {}
gates1 = []
summits1 = []


def solution(n, paths, gates, summits):
    global graphs, gates1, summits1
    gates1 = set(gates)
    summits1 = set(summits)
    graphs = {i: {} for i in range(1, n + 1)}
    for i, j, w in paths:
        graphs[i][j] = w
        graphs[j][i] = w

    for start in gates:
        recusion(start, 0, start)



    answer = [ans_top, ans_distance]
    return answer


print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
