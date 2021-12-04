import itertools


def solution(user_id, banned_id):
    user_id.sort(key=lambda x: len(x))
    banned_id.sort(key=lambda x: len(x))
    answer = 0
    dict_list = []
    length_list = []
    for user in banned_id:
        bad_user_length = len(user)
        bad_user_dict = {}
        for i in range(len(user)):
            if user[i] != '*':
                bad_user_dict[i] = user[i]
        dict_list.append(bad_user_dict)
        length_list.append(bad_user_length)
    candidate = list(itertools.permutations(user_id, len(banned_id)))
    # print(candidate)
    # print(dict_list)
    # print(length_list)
    ans_list = []
    for i in range(len(candidate)):
        flag = False
        for j in range(len(dict_list)):
            if len(candidate[i][j]) != length_list[j]:
                break
            # print(flag)
            if flag:
                break
            # print(candidate[i])
            # print(candidate[i][j])
            # print(dict_list[j])
            # print()
            for k in dict_list[j]:
                if candidate[i][j][k] != dict_list[j][k]:
                    flag = True
                    break
            if flag:
                break
        else:
            # print('else', candidate[i])
            # print()
            temp = list(candidate[i])
            temp.sort(key=lambda x: [len(x), x])
            if temp not in ans_list:
                ans_list.append(temp)
                answer += 1
    # print(ans_list)

    # print(dict_list)
    # print(length_list)

    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
