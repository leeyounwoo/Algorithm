import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = 100
    result = 0

    row_lst = []
    for i in range(len(N)):
        chr = input()
        row_lst.append(chr)
        print(chr)
