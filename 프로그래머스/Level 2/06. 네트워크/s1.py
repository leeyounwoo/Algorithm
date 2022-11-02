def solution(n, computers):
    def bfs(index):
        for num in linked_list[index]:
            if checked[num]:
                continue
            else:
                checked[num] = True
                bfs(num)
        return

    checked = [False] * n
    linked_list = []
    for i in range(n):
        temp = []
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                temp.append(j)
        linked_list.append(temp)

    answer = 0
    for i in range(n):
        if checked[i]:
            continue
        else:
            answer += 1
            bfs(i)
    return answer


print(solution(3, [[1,1,0], [1,1,0], [0,0,1]]))