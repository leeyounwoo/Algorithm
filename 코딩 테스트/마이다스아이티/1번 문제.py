def solution(H):
    # 각 높이에 따른 index값
    indexs = {}
    for i in range(len(H)):
        if H[i] in indexs:
            indexs[H[i]].append(i)
        else:
            indexs[H[i]] = [i]
    set_hight = sorted(list(set(H)))
    length = len(H)
    answer = [[i, 0] for i in set_hight]
    for temp_list in answer:
        level = temp_list[0]
        for start_index in range(length):
            for i in range(length - start_index):
                end_index = start_index + i
                temp = H[start_index:end_index+1]

                min_temp = min(temp)
                if min_temp == level:

                    answer[level-1][1] += 1
    return answer

print(solution([3, 1, 2, 1 ]))