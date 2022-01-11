import sys
sys.stdin = open('1014/woosteelz/1251_하나로/input.txt')

for tc in range(int(input())):
    graph = [[0 for _ in range(1000001)] for _ in range(1000001)]
    N = int(input())
    node_x = list(map(int, input().split()))
    node_y = list(map(int, input().split()))
    E = float(input())
    # node = list(zip(node_x, node_y))
    print(node_x)
    # print(f'#{tc+1} {}')
