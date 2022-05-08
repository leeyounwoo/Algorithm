def recusion(prev, intensity, flag_top, start_gate, false_list, true_list, top):
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
            # 이미 간 적이 있으면 X
            if flag_top:
                continue
            # 간 적이 없으면
            else:
                recusion(next, next_intensity, True, start_gate, false_list, true_list, next)

        # 출입구라면
        elif next in gates1:
            # 이미 산봉우리를 다녀왔고 시작 출입구와 같으면 확인
            if next == start_gate and flag_top:
                if next_intensity < ans_distance:
                    ans_top = top
                    ans_distance = next_intensity
                if next_intensity == ans_distance and top < ans_top:
                    ans_top = top
                    ans_distance = next_intensity
                return
            else:
                continue

        # 쉼터
        else:
            if flag_top and not true_list[next]:
                if intensity < next_intensity:
                    continue
                true_list[next] = True
                recusion(next, next_intensity, flag_top, start_gate, false_list, true_list, top)
                true_list[next] = False
            elif not flag_top and not false_list[next]:
                false_list[next] = True
                recusion(next, next_intensity, flag_top, start_gate, false_list, true_list, top)
                false_list[next] = False


ans_top = -1
ans_distance = 10000001
graphs = {}
gates1 = []
summits1 = []


def solution(n, paths, gates, summits):
    global graphs, gates1, summits1
    gates1 = gates
    summits1 = summits
    graphs = {i: {} for i in range(1, n + 1)}
    for i, j, w in paths:
        graphs[i][j] = w
        graphs[j][i] = w

    for start in gates:
        recusion(start, 0, False, start, {i: False for i in range(1, n + 1)}, {i: False for i in range(1, n + 1)}, 0)



    answer = [ans_top, ans_distance]
    return answer


# print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
