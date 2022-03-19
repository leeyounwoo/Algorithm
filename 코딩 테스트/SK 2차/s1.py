def solution(goods):
    answer = []
    temp = {}
    max_length = 0
    for i in range(len(goods)):
        if max_length < len(goods[i]):
            max_length = len(goods[i])
    total = {key:[] for key in range(1, max_length+1)}

    for i in range(len(goods)):
        sub_string = {key:[] for key in range(1, len(goods[i]) + 1)}
        z = []
        for a in range(len(goods[i])):
            for b in range(a+1, len(goods[i]) + 1):
                z.append(goods[i][a:b])
        z = list(set(z))
        for k in range(len(z)):
            total[len(z[k])].append(z[k])
            sub_string[len(z[k])].append(z[k])

        temp[goods[i]] = sub_string
        temp[goods[i]] = sub_string

    for key in goods:
        a_list = []
        flag = False
        for i in range(1, len(key) + 1):
            for j in range(len(temp[key][i])):
                if total[i].count(temp[key][i][j]) == 1:
                    a_list.append(temp[key][i][j])
                    flag = True
            if flag:
                break
        if flag:
            answer.append(' '.join(sorted(a_list)))
        else:
            answer.append("None")


    return answer

print(solution(["pencil","pencil","pencil","pencil"]))
print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))
