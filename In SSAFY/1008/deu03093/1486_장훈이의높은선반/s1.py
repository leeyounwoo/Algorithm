import sys
sys.stdin = open('input.txt')

for T in range(1, 1+int(input())):
    N, B = map(int, input().split())
    hights = list(map(int, input().split()))
