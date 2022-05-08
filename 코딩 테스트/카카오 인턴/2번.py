from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q = sum(queue1) + sum(queue2)
    flag = sum_q // 2
    if sum_q % 2:
        return -1

    ans = 0
    sum1 = sum(q1)
    sum2 = sum(q2)
    already = set()
    while True:
        if sum1 == flag:
            return ans
        else:
            temp = tuple(q1)
            if ans != 0 and temp in already:
                return -1
            else:
                already.add(temp)

            if sum1 > sum2:
                temp = q1.popleft()
                q2.append(temp)
                sum2 += temp
                sum1 -= temp

            else:
                temp = q2.popleft()
                q1.append(temp)
                sum2 -= temp
                sum1 += temp
        ans += 1

    return ans