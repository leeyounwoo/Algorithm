import sys

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers[0] * numbers[-1])