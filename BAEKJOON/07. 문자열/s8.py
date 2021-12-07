s = input()

ans = 0
for i in range(len(s)):
    temp = ord(s[i])
    if 65 <= temp <= 67:
        ans += 3
    elif 68 <= temp <= 70:
        ans += 4
    elif 71 <= temp <= 73:
        ans += 5
    elif 74 <= temp <= 76:
        ans += 6
    elif 77 <= temp <= 79:
        ans += 7
    elif 80 <= temp <= 83:
        ans += 8
    elif 84 <= temp <= 86:
        ans += 9
    elif 87 <= temp:
        ans += 10
print(ans)


