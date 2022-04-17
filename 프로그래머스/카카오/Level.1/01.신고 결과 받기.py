def solution(id_list, report, k):
    receive = {user: [] for user in id_list}
    send = {user: [] for user in id_list}
    for temp in report:
        a, b = map(str, temp.split())
        if a not in receive[b]:
            receive[b].append(a)
        if b not in send[a]:
            send[a].append(b)

    cannot = []
    for user in id_list:
        if len(receive[user]) >= k:
            cannot.append(user)

    answer = []
    for user in id_list:
        cnt = 0
        for temp in send[user]:
            if temp in cannot:
                cnt += 1
        answer.append(cnt)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))