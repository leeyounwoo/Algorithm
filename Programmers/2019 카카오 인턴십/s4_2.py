def solution(stones, k):
    answer = 0
    while True:
        flag = False
        min_value = 200000000
        for i in range(1, len(stones)):
            if stones[i] > 0:
                if min_value > stones[i]:
                    min_value = stones[i]

        for i in range(len(stones)):
            if stones[i]:
                stones[i] -= min_value

        # 현재 상태가 이동 가능한지 확인
        # print(stones)
        start = -1
        end = len(stones)
        while start < end:
            # print(start)
            for i in range(start+1, start+k+1):
                if i >= end:
                    start = i
                    # print(123, start)
                    break
                if stones[i]:
                    start = i
                    break
            # 현재 상태 불가능
            else:
                flag = True
                break
        if flag:
            answer += min_value
            break
        else:
            answer += min_value
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))