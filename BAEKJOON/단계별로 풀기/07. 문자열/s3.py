s = input()
ans = [-1] * 26
for i in range(len(s)):
    if ans[ord(s[i]) - 97] == -1:
        ans[ord(s[i]) - 97] = i
print(' '.join(str(i) for i in ans))