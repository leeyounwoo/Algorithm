def dfs(stones, flag, k):
    # print(stones)
    global answer
    cnt_k = 0
    cnt_zero = 0
    minus = 0
    for a in stones:
        if a == 0:
            cnt_zero += 1
        elif a == k:
            cnt_k += 1
        elif a < 0:
            minus += 1
            break
    if minus:
        return
    if cnt_k == 1 and cnt_zero == len(stones) - 1:
        # print(flag)
        answer = flag
        # answer.append(flag)
        return
    elif cnt_zero >= 2:
        return
    elif cnt_zero == 1:
        zero_index = stones.index(0)
        for i in range(len(stones)):
            if i == zero_index:
                stones[i] += 1
            else:
                stones[i] -= 1
        flag += str(zero_index)
        # print('456', cnt_zero)
        dfs(stones, flag, k)
    else:
        for i in range(len(stones)-1, -1, -1):
            for j in range(len(stones)):
                if j == i:
                    stones[j] += 1
                else:
                    stones[j] -= 1
            flag += str(i)
            # print('123',cnt_zero)
            # print(stones)
            dfs(stones, flag, k)


answer = ''
def solution(stones, k):
    global answer
    dfs(stones, '', k)
    return answer



print(solution([0, 2, 3], 3))
print(solution([4, 2, 2, 1, 4], 1))
print(solution([5, 7, 2, 4, 9], 20))