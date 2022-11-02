from heapq import heappush, nlargest, nsmallest
def solution(operations):
    answer = []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heappush(answer, num)
        else:
            if num == 1:
                answer = nlargest(len(answer), answer)[1:]
            else:
                answer = nsmallest(len(answer), answer)[1:]
    if len(answer) == 0:
        return [0, 0]
    else:
        return [nlargest(1, answer)[0], nsmallest(1, answer)[0]]