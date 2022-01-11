import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    size = int(input())
    maze = [list(map(int, input())) for _ in range(size)]
    wall = [[0]*size for _ in range(size)]
