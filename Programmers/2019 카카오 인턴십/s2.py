def solution(s):
    string = s[1:-1]
    total = []
    middle = []
    part = ''
    flag_part = 0
    for i in range(len(string)):
        if flag_part == 0:
            if string[i] == '{':
                # print(i)
                flag_part = 1
            else:
                continue
        else:
            if string[i] == ',':
                middle.append(int(part))
                part = ''
            elif string[i] == '}':
                middle.append(int(part))
                part = ''
                total.append(middle)
                middle = []
                flag_part = 0
            else:
                part += string[i]

    total.sort(key=lambda x: len(x))
    # print(total)
    answer = [total[0][0]]
    for i in range(1, len(total)):
        for ans in answer:
            # print(ans)
            total[i].remove(ans)
        # print(total[i])
        answer.append(total[i][0])
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))