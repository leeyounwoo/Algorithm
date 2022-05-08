def solution(rooms, target):
    # 정답을 담을 배열
    answer = []

    # 개인이 차지하고 있는 사무실들의 배열을 담을 딕셔너리
    peoples_room_dict = {}
    # 개인이 차지하고 있는 사무실의 개수를 담을 딕셔너리
    people_cnt = {}
    for i in range(len(rooms)):
        room_num = ''
        flag = 0
        for j in range(1, len(rooms[i])):
            if rooms[i][j] == ']':
                flag = j
                break
            else:
                room_num += rooms[i][j]
        peoples = rooms[i][flag+1:].split(',')
        room_num = int(room_num)
        for people in peoples:
            if people not in peoples_room_dict:
                peoples_room_dict[people] = [room_num]
                people_cnt[people] = 1
            else:
                peoples_room_dict[people].append(room_num)
                people_cnt[people] += 1

    # key: 차지하고 있는 사무실 수, value: {이름: 사무실과의 거리}
    candidate = {}
    for key, value in people_cnt.items():
        if value not in candidate:
            candidate[value] = {key: 0}
        else:
            candidate[value][key] = 0
    for key in sorted(candidate.keys()):
        for people in candidate[key]:
            temp = 1000000
            for room in peoples_room_dict[people]:
                a = abs(room - target)
                if a < temp:
                    temp = a
            candidate[key][people] = temp

    # key: 차지하고 있는 사무실 수, value: {사무실과의 거리: [이름들(사전순으로 정렬)]}
    final = {}
    for key in sorted(candidate.keys()):
        if key not in final:
            temp = {}
            for key1, value in candidate[key].items():
                if value not in temp:
                    temp[value] = [key1]
                else:
                    temp[value].append(key1)
            for a in temp.keys():
                temp[a].sort()
            final[key] = temp

    # 같은 사무실에 있는 경우 제외하고 우선순위대로 answer 에 추가
    for key in sorted(candidate.keys()):
        for key1 in sorted(final[key].keys()):
            if key1 == 0:
                continue
            else:
                for key2 in final[key][key1]:
                    answer.append(key2)

    return answer

print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403))