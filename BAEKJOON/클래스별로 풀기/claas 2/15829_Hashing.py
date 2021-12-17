n = int(input())
word = input()
ans = 0
flag = 1
for i in range(len(word)):
    ans += (ord(word[i]) - 96) * flag
    flag *= 31
ans %= 1234567891
print(ans)