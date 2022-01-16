import sys
from itertools import product

def input():
    return sys.stdin.readline().rstrip()


def isPosible(num):
    numbers = str(num)
    for i in range(len(numbers)):
        if not buttons[int(numbers[i])]:
            return False
    return True


sys.stdin = open('input.txt')
goal = input()
n = int(input())
buttons = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
broken = set(list(map(int, input().split())))
buttons = list(buttons - broken)
ans = abs(100 - int(goal))
for i in range(len(goal)-1, len(goal)+2):
    for comb in product(buttons, repeat=i):
        comb = list(comb)
        num = ''
        for c in comb:
            num += str(c)
        if num:
            flag = abs(int(goal) - int(num)) + i
            if flag < ans:
                ans = flag

print(ans)


