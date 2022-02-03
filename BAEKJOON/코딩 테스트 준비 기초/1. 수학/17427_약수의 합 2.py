import sys

def input():
    return sys.stdin.readline().rstrip()


def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()

    return divisorsList


sys.stdin = open('input.txt')
n = int(input())
ans = 0
for i in range(n, -1, -1):
    ans += sum(getMyDivisor(i))
print(ans)
