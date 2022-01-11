import sys

def pattern_search(p, s):
    window = len(p)
    for i in range(len(s)-window):
        if p == s[i:i+window]:
            return 1
    return 0
    # ans = 0
    # for i in range(len(s)):
    #     if p[0] == word[i]:
    #         for j in range(1, len(p)):
    #             if (i + j) >= len(s) or s[i + j] != p[j]:
    #                 break
    #         else:
    #             ans = 1
    #             break
    # return ans


sys.stdin = open('input.txt')
for T in range(1, 1 + int(input())):
    pattern = input()
    word = input()
    ans = pattern_search(pattern, word)
    print('#{} {}'.format(T, ans))