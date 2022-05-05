from copy import copy
from collections import deque

def solution(gems):
    copy_checked = {}
    # 효율성에서 틀린 부분
    size = len(set(gems))
    for temp in gems:
        if temp not in copy_checked:
            copy_checked[temp] = False

    checked1 = copy(copy_checked)

    start, end = 0, 0
    cnt = 0
    for i in range(len(gems)):
        if not checked1[gems[i]]:
            checked1[gems[i]] = True
            cnt += 1
            if cnt == size:
                end = i
                break

    checked = copy(copy_checked)
    cnt = 0
    for i in range(end, -1, -1):
        temp = gems[i]
        if not checked[temp]:
            checked[temp] = True
            cnt += 1
            if cnt == size:
                start = i
                break

    words = deque(gems[start:end+1])
    ans_start = start
    ans_end = end
    for i in range(end+1, len(gems)):
        if ans_end - ans_start + 1 == len(checked):
            break
        words.append(gems[i])
        if words[0] == words[-1]:
            checked = copy(copy_checked)
            cnt = 0
            for j in range(i, start, -1):
                if not checked[gems[j]]:
                    checked[gems[j]] = True
                    cnt += 1
                    if cnt == size:
                        words = gems[j:i+1]
                        start = j
                        if i - j < ans_end - ans_start:
                            ans_start = j
                            ans_end = i
                        break


    answer = [ans_start+1, ans_end+1]

    return answer