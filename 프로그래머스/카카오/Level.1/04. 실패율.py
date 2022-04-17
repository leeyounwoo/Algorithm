def solution(N, stages):
    levels = {i: 0 for i in range(1, N+2)}
    stages.sort(reverse=True)
    for level in levels.keys():
        if level in stages:
            # print(level, stages.count(level), stages.index(level)+stages.count(level))
            levels[level] = float(stages.count(level)) / (stages.index(level) + stages.count(level))
    new = sorted(levels.items(), key=lambda x: x[1], reverse=True)
    ans = [key[0] for key in new]
    if N+1 in ans:
        ans.remove(N+1)

    return ans

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))