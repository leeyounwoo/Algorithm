def dfs(now, checked, flag):
    global answer
    for i in range(len(words1)):
        # 이미 접근했던 단어이면 pass
        if checked[i]:
            continue

        # 접근한 적이 없는 단어
        same_cnt = 0
        for j in range(len(now)):
            if now[j] == words1[i][j]:
                same_cnt += 1
        # 한 글자만 다른 경우
        if same_cnt == len(now) - 1:
            # 원하는 단어인 경우
            if words1[i] == target1:
                if flag < answer:
                    answer = flag
                    return
            else:
                if flag + 1 == len(words1):
                    return
                checked[i] = True
                dfs(words1[i], checked, flag + 1)
        else:
            continue
def solution(begin, target, words):
    global answer
    global target1
    global words1
    target1 = target
    words1 = words
    answer = len(words)

    checked = [False] * len(words)
    dfs(begin, checked, 1)
    if answer == len(words):
        return 0

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))