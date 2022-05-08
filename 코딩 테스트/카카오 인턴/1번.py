def solution(survey, choices):
    answer = ['R', 'C', 'J', 'A']
    select = {1: [0, 3], 2: [0, 2], 3: [0, 1], 4: [0, 0], 5: [1, 1], 6: [1, 2], 7: [1, 3]}
    ans = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    for i in range(len(survey)):
        choice = choices[i]
        temp = select[choice]
        a, score = temp[0], temp[1]
        ans[survey[i][a]] += score
    print(ans)
    if ans['T'] > ans['R']:
        answer[0] = 'T'
    if ans['F'] > ans['C']:
        answer[1] = 'F'
    if ans['M'] > ans['J']:
        answer[2] = 'M'
    if ans['N'] > ans['A']:
        answer[3] = 'N'

    return ''.join(answer)


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# print(solution())
# print(solution())
# print(solution())

