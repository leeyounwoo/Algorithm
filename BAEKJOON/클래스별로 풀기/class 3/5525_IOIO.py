import sys

sys.stdin = open('input.txt')
n = int(input())
n *= 2
n += 1
m = int(input())
words = input()

pattern = ''
for i in range(n):
    if i % 2:
        pattern += 'O'
    else:
        pattern += 'I'

ans = 0
start = 0
end = n
# print(words[start:end])
while end < m:
    if words[start:end] == pattern:
        ans += 1
    start += 1
    end += 1
print(ans)