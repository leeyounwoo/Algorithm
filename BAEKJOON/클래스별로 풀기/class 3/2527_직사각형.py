import sys


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if p2 < x1 or y2 > q1 or x2 > p1 or p2 < x2 or y1 > q2:
        ans = 'd'
    elif (p2 == x1 and y2 == q1) or (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2) or (p2 == x1 and q2 == y1):
        ans = 'c'
    elif ((x1 == p2 and y2 < q1) or (y2 == q1 and p2 > x1)) or ((p1 == x2 and q1 > y2) or (q1 == y2 and x2 < p1)) or ((p1 == x2 and q2 > y1) or (y1 == q2 and x2 < p1)) or ((p2 == x1 and q2 > y1) or (q2 == y1 and p2 > x1)):
        ans = 'b'
    else:
        ans = 'a'

    print(ans)