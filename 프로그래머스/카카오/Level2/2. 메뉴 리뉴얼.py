from itertools import combinations

def solution(orders, course):
    answer = []
    candidate = {}
    for i in range(len(orders)):
        for j in range(2, len(orders[i])+1):
            for com in combinations(orders[i], j):
                # key = sorted(com)
                key = ''.join(sorted(com))
                if key not in candidate:
                    candidate[key] = 1
                else:
                    candidate[key] += 1

    temp_answer = {}
    for key, value in candidate.items():
        if len(key) not in temp_answer:
            temp_answer[len(key)] = [key, value]
        elif temp_answer[len(key)][1] < value:
            temp_answer[len(key)] = [key, value]
        elif temp_answer[len(key)][1] == value:
            temp_answer[len(key)].extend([key, value])

    for key, value_list in temp_answer.items():
        if key in course:
            for i in range(0, len(value_list), 2):
                if value_list[i+1] >= 2:
                    answer.append(value_list[i])
    answer.sort()

    return answer

print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))