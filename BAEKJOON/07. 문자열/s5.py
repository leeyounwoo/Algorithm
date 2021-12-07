s = input()
ans = [0] * 26

for i in range(len(s)):
    temp = ord(s[i])
    if 97 <= temp <= 122:
        ans[temp-97] += 1
    elif 65 <= temp <= 90:
        ans[temp-65] += 1

if ans.count(max(ans)) >= 2:
    print('?')
else:
    print(chr(65+ans.index(max(ans))))