def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        flag = ''
        temp = ''
        number = 1
        for start in range(0, len(s), i):
            now = s[start:start+i]
            if start == 0:
                temp = s[start:start+i]
                number = 1
            else:
                # 문자열이 같음
                if temp == now:
                    number += 1
                # 문자열이 다름
                else:
                    # 1개만 있음
                    if number == 1:
                        flag += temp
                    # 2개 이상
                    else:
                        flag += str(number) + temp
                    number = 1
                    temp = now
        # 마지막꺼 추가
        if temp == now:
            if number == 1:
                flag += temp
            else:
                flag += str(number) + temp
        else:
            flag += temp
        cnt = len(flag)
        if answer > cnt:
            answer = cnt

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

