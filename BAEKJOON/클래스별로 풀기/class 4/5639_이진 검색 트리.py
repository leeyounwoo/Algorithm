import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
pattern1 = input()
alpha1 = {}
for word in pattern1:
    if word in alpha1:
        alpha1[word] += 1
    else:
        alpha1[word] = 1
print(alpha1)

pattern2 = input()
alpha2 = {}
for word in pattern2:
    if word in alpha2:
        alpha2[word] += 1
    else:
        alpha2[word] = 1
print(alpha2)

ans = 0
if len(alpha1.keys()) < len(alpha2.keys()):
    for key in alpha1.keys():
        if key in alpha2:
            ans += min(alpha1[key], alpha2[key])

else:
    for key in alpha2.keys():
        if key in alpha1:
            ans += min(alpha1[key], alpha2[key])
print(ans)