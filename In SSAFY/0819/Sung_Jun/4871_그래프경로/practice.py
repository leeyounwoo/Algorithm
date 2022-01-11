import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1):
    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())

    check = {key : [] for key in range(1, V+1)}
    for tem in temp:
        check[tem[0]].append(tem[1])

    stack = [start]
    visited = []
    while stack:
        next_nod = stack.pop()
        if next_nod == end:
            print('옳다')
            break

        if next_nod not in visited:
            visited.append(next_nod)
            for w in check[next_nod]:
                stack.append(w)

    print(visited)








