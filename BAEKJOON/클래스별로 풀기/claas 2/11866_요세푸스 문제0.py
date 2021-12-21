import sys

sys.stdin = open('input.txt')
n, k = map(int, input().split())
people = [i+1 for i in range(n)]
kill = k - 1
ans = []
k -= 1
while people:
    ans.append(str(people.pop(kill)))
    kill += k
    if not people:
        break
    kill %= len(people)
print('<{}>'.format(', '.join(ans)))