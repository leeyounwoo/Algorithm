def solution(stones, k):
    end = len(stones)
    min_value = min(stones)

    for i in range(len(stones)):
        stones[i] -= min_value
    answer = min_value

    while True:
        start = -1
        flag = False
        while start < end:
            for i in range(start+1, start+k+1):
                if i >= end:
                    start = i
                    break
                if stones[i]:
                    stones[i] -= 1
                    start = i
                    break
            else:
                flag = True
                break
        if flag:
            break
        answer += 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))