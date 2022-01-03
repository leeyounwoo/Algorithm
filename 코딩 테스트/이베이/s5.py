from itertools import combinations
def isPalindrome(word1, word2):
    flag1 = word1 + word2
    flag2 = word2 + word1
    if flag1 == flag1[::-1] or flag2 == flag2[::-1]:
        return True
    else:
        return False


def solution(P):
    words_list = P
    ans = []
    num1 = words_list.pop(0)
    for num2 in words_list:
        temp_words_list = words_list[:]
        temp_words_list.remove(num2)
        if isPalindrome(num1, num2):
            temp = []
            indexs = [i for i in range(len(temp_words_list))]
            for com in combinations(indexs, 2):
                temp.append(com)
            length = len(temp_words_list)
            a = []
            for com in combinations(temp, length // 2):
                check = [False] * length
                flag_com = False
                for i in range(len(com)):
                    if check[com[i][0]] or check[com[i][1]]:
                        flag_com = True
                        break
                    check[com[i][0]] = True
                    check[com[i][1]] = True
                if flag_com:
                    continue
                a.append(com)

            for com in a:
                for b in com:
                    if not isPalindrome(temp_words_list[b[0]], temp_words_list[b[1]]):
                        break
                else:
                    ans.append(num2)
                    break
        else:
            continue

    return ans

print(solution(["11","111","11","211"]))
# print(solution(["21","123","111","11"]))
