import sys
sys.stdin = open('input.txt')

# 내가적은건 이건 BFS라 DFS사용해야되... (미숙)
# 재귀함수를 통해 DFS활용해보...자아...
def chase(end_x,end_y):
    # 끝나는지점에서 시작할꺼다.
    flag = False
    visited[end_x][end_y] = 1
    while stack:
        print(stack.pop())

        for i in range(4):
            new_y = end_y + dy[i]
            new_x = end_x + dx[i]
            if box[new_x][new_y] == 2:
                return 1
                flag = True
                break
            elif box[new_x][new_y] == 0 and visited[new_x][new_y]:
                stack.append((new_x,new_y))
                return chase(new_x, new_y)
        if flag:
            break

for tc in range(1,11):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    T = int(input())
    box = []

    # 박스 만들기
    for _ in range(16):
        box.append(list(map(int,input())))
    visited = [[0]*16 for _ in range(16)]
    # 끝나는 지점부터 시작할꺼야! 끝나는지점 어디야~
    for j in range(16):
        for i in range(16):
            if box[j][i] == 3:
                end_y, end_x = j, i
    stack = [(end_x,end_y)]
    print(chase(end_x,end_y))



