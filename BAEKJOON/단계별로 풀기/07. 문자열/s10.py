words = [input() for _ in range(int(input()))]

ans = 0
for i in range(len(words)):
    # 각 단어에 대해서 초기화
    check = [False] * 26
    flag = -1
    for j in range(len(words[i])):
        temp = ord(words[i][j]) - 97
        # 처음나온 알파벳이면 상관없음
        if not check[temp]:
            flag = temp
            check[temp] = True
            continue
        # 처음나온 알파벳이 아니어도 직전에 나왔던거라면 상관없음
        elif flag == temp:
            continue
        # 처음나온 알파벳도 아닌데 직전에 나온것도 아니라면 안됌
        else:
            break
    else:
        ans += 1
print(ans)
