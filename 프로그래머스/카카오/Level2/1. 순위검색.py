def solution(info, query):
    answer = []
    people_cnt = {'cpp':
                      {'backend':
                           {'junior':
                                {'chicken': [], 'pizza': []},
                            'senior': {'chicken': [], 'pizza': []}},
                       'frontend':
                           {'junior':
                                {'chicken': [], 'pizza': []},
                            'senior': {'chicken': [], 'pizza': []}}},
                  'java':
                      {'backend':
                           {'junior':
                                {'chicken': [], 'pizza': []},
                            'senior': {'chicken': [], 'pizza': []}},
                       'frontend':
                           {'junior':
                                {'chicken': [], 'pizza': []},
                            'senior': {'chicken': [], 'pizza': []}}},
                  'python':
                      {'backend':
                           {'junior':
                                {'chicken': [], 'pizza': []},
                            'senior': {'chicken': [], 'pizza': []}},
                       'frontend':
                           {'junior':
                                {'chicken': [], 'pizza': []},
                            'senior': {'chicken': [], 'pizza': []}}},
                  }
    for i in range(len(info)):
        a, b, c, d, score = map(str, info[i].split())
        score = int(score)
        people_cnt[a][b][c][d].append(score)

    print(people_cnt)

    for i in range(len(query)):
        a, temp, b, temp, c, temp, d, flag = map(str, query[i].split())
        flag = int(flag)

        if a == '-':
            keys_a = ['cpp', 'java', 'python']
        else:
            keys_a = [a]

        if b == '-':
            keys_b = ['backend', 'frontend']
        else:
            keys_b = [b]

        if c == '-':
            keys_c = ['junior', 'senior']
        else:
            keys_c = [c]

        if d == '-':
            keys_d = ['chicken', 'pizza']
        else:
            keys_d = [d]

        cnt = 0

        for ka in keys_a:
            for kb in keys_b:
                for kc in keys_c:
                    for kd in keys_d:
                        for score in people_cnt[ka][kb][kc][kd]:
                            if score >= flag:
                                cnt += 1

        answer.append(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))