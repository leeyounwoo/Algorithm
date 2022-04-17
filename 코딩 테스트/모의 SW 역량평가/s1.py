import sys
sys.stdin = open('input.txt')

def get_neighboor(j, i, max_j, max_i):
    list = []
    if i-1 >= 0:
        list.append([j, i-1])
    if j+1 < max_j and i-1 >= 0:
        list.append([j+1, i-1])
    if j+1 < max_j:
        list.append([j+1, i])
    if i+1 < max_i:
        list.append([j, i+1])
    if j-1 >= 0:
        list.append([j-1, i])
    if j-1 >= 0 and i-1 >= 0:
        list.append([j-1, i-1])
    return list



for T in range(1, 1+int(input())):
    MAX_J, MAX_I = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(MAX_I)]
    check = [[False] * MAX_J for _ in range(MAX_I)]
    ans = 0
    start_i, start_j = 0, 0
    print(check)
