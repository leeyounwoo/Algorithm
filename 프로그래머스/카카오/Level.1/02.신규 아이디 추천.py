def function1(new_id):
    new_id = list(new_id)
    for i in range(len(new_id)):
        temp = ord(new_id[i])
        if 65 <= temp <= 90:
            new_id[i] = chr(temp + 32)


def solution(new_id):
    new_id = list(new_id)
    # 1 번째
    for i in range(len(new_id)):
        temp = ord(new_id[i])
        if 65 <= temp <= 90:
            new_id[i] = chr(temp + 32)

    # print('0: {}, 9: {}, a: {}, z: {}, -: {}, _: {}, .:{}'.format(ord('0'), ord('9'), ord('a'), ord('z'), ord('-'), ord('_'), ord('.')))

    # 2 번째
    pop_list = []
    for i in range(len(new_id)):
        temp = ord(new_id[i])
        if not (48 <= temp <= 57 or 97 <= temp <= 122 or temp in [45, 95, 46]):
            pop_list.append(i)

    for i in range(len(pop_list)-1, -1, -1):
        # print(new_id[pop_list[i]])
        new_id.pop(pop_list[i])
    # print(new_id)

    # 3 번째
    flag = False
    for i in range(len(new_id)-1, -1, -1):
        if new_id[i] == ".":
            if flag:
                new_id.pop(i)
            flag = True

        else:
            flag = False
    # print(new_id)

    # 4 번째
    if new_id[0] == '.':
        new_id.pop(0)
    if new_id and new_id[-1] == '.':
        new_id.pop()
    # print(new_id)

    # 5 번째
    if len(new_id) == 0:
        new_id = ['a']

    # 6 번쨰
    # new_id = [i for i in range(1, 16)]
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id.pop()

    # 7 번째
    if len(new_id) <= 2:
        new_id.extend([new_id[-1]] * (3-len(new_id)))

    return ''.join(new_id)

print(solution("=.="))