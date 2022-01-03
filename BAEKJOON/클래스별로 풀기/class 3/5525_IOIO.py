import sys


def BruteForce(t, p):
    n, m = len(t), len(p)
    i, j = 0, 0
    while i < n and j < m:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == m:
        return i-m
    else:
        return -1


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

print(pattern, words)
print(BruteForce(words, pattern))