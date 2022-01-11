import sys
sys.stdin = open('input.txt')

number = int(input())

numbers = list(map(int, input().split()))

T = int(input())

for tc in range(T):
    numbers = list(map(int, input().split()))