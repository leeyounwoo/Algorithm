from heapq import heappush, nlargest, heappop

def solution(A, B):
    array_a = []
    array_b = []
    for num in A:
        heappush(array_a, -num)
    for num in B:
        heappush(array_b, -num)

    answer = 0
    while len(array_a):
        max_a = -1 * heappop(array_a)
        max_b = -1 * heappop(array_b)
        if max_b <= max_a:
            heappush(array_b, -max_b)
        else:
            answer += 1
    # while len(array_a) and len(array_b):
    #     max_a = heappop(array_a)
    #     array_a = nlargest(len(array_a), array_a)[1:]
    #     max_b = nlargest(1, array_b)[0]
    #     if max_b > max_a:
    #         array_b = nlargest(len(array_b), array_b)[1:]
    #         answer += 1

    return answer

print(solution([5,1,3,7], [2,2,6,8]))