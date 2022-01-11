import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N*M
    code = [[] for _ in range(N)]

    hex_bi = {
        '0': [0, 0, 0, 0],
        '1': [0, 0, 0, 1],
        '2': [0, 0, 1, 0],
        '3': [0, 0, 1, 1],
        '4': [0, 1, 0, 0],
        '5': [0, 1, 0, 1],
        '6': [0, 1, 1, 0],
        '7': [0, 1, 1, 1],
        '8': [1, 0, 0, 0],
        '9': [1, 0, 0, 1],
        'A': [1, 0, 1, 0],
        'B': [1, 0, 1, 1],
        'C': [1, 1, 0, 0],
        'D': [1, 1, 0, 1],
        'E': [1, 1, 1, 0],
        'F': [1, 1, 1, 1]
    }

    for i in range(N):
        row = input()
        for j in range(M):
            hex_bi[row[j]])
