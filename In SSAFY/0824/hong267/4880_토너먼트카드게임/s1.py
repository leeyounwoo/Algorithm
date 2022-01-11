import sys

sys.stdin = open('input.txt')

def rsp(list1, n):
    if n == 2:
        if list1[0] == 1 and list1[1] == 3:
            return list1[0]
        elif list1[0] == 3 and list1[1] == 1:
            return list1[1]
        elif list1[0] > list1[1]:
            return list1[0]
        elif list1[1] > list1[0]:
            return list1[1]
        else:
            return list1[0]

    i = len(list1) // 2
    if rsp(list1[:i], len(list[:i])) == 1 and rsp(list1[i:], len(list[i:])) == 3:
        return rsp(list1[:i], len(list[:i]))
    elif rsp(list1[:i], len(list[:i])) == 3 and rsp(list1[i:], len(list[i:])) == 1:
        return rsp(list1[i:], len(list[i:]))
    elif rsp(list1[:i], len(list[:i])) > rsp(list1[i:], len(list[i:])):
        return rsp(list1[:i], len(list[:i]))
    elif rsp(list1[:i], len(list[:i])) < rsp(list1[i:], len(list[i:])):
        return rsp(list1[i:], len(list[i:]))
    else:
        return rsp(list1[:i], len(list[:i]))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print(rsp(cards, N))
