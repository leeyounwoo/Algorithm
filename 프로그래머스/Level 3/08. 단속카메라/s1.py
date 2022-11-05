from copy import deepcopy


def solution(routes):
    cnt = [0] * 60001
    a = {}
    for i in range(len(routes)):
        start = min(routes[i]) + 30000
        end = max(routes[i]) + 30000
        for j in range(start, end+1):
            cnt[j] += 1
            if j in a:
                a[j].append(i)
            else:
                a[j] = [i]

    answer = 0
    while sum(cnt):
        answer += 1
        max_index = cnt.index(max(cnt))
        delete_list = deepcopy(a[max_index])
        for i in delete_list:
            start = min(routes[i]) + 30000
            end = max(routes[i]) + 30000
            for j in range(start, end+1):
                cnt[j] -= 1
                a[j].remove(i)

    return answer


print(solution([[1, 2], [3, 4], [1, 5]]))