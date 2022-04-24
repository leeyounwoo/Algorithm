from bisect import bisect_left

def solution(info, query):
    answer = []
    people_cnt = {
        'cpp': {
            'backend':{
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            'frontend':{
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-':[]
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            '-': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-':[]
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            }
        },
        'java': {
            'backend': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            '-': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            }
        },
        'python': {
            'backend': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            '-': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            }
        },
        '-': {
            'backend': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            'frontend': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            },
            '-': {
                'junior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                'senior': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                },
                '-': {
                    'chicken': [],
                    'pizza': [],
                    '-': []
                }
            }
        }
    }

    for i in range(len(info)):
        a, b, c, d, score = map(str, info[i].split())
        score = int(score)
        people_cnt[a][b][c][d].append(score)
        people_cnt['-'][b][c][d].append(score)
        people_cnt[a]['-'][c][d].append(score)
        people_cnt[a][b]['-'][d].append(score)
        people_cnt[a][b][c]['-'].append(score)
        people_cnt['-']['-'][c][d].append(score)
        people_cnt['-'][b]['-'][d].append(score)
        people_cnt['-'][b][c]['-'].append(score)
        people_cnt[a]['-']['-'][d].append(score)
        people_cnt[a]['-'][c]['-'].append(score)
        people_cnt[a][b]['-']['-'].append(score)
        people_cnt['-']['-']['-'][d].append(score)
        people_cnt['-']['-'][c]['-'].append(score)
        people_cnt['-'][b]['-']['-'].append(score)
        people_cnt[a]['-']['-']['-'].append(score)
        people_cnt['-']['-']['-']['-'].append(score)

    for a1 in people_cnt.keys():
        for b1 in people_cnt[a1].keys():
            for c1 in people_cnt[a1][b1].keys():
                for d1 in people_cnt[a1][b1][c1].keys():
                    people_cnt[a1][b1][c1][d1].sort()

    for q in query:
        l, _, p, _, c, _, f, point = q.split()
        i = bisect_left(people_cnt[l][p][c][f], int(point))
        answer.append(len(people_cnt[l][p][c][f]) - i)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))