import sys
sys.stdin = open('input.txt')

# 두 번째 방법
def calc(v):
    if len(tree[v]) == 2: # 단말노드 2개가 있다면, 정점번호와 피연산자가 들어있음
        return int(tree[v][1])
    else: # 연산자
        L = calc(int(tree[v][2]))
        R = calc(int(tree[v][3]))

        if tree[v][1] == '+' : return L+R
        elif tree[v][1] == '-' : return L-R
        elif tree[v][1] == '*' : return L*R
        elif tree[v][1] == '/' : return L/R

for tc in range(1, 11):
    N = int(input()) # 정점의 개수
    tree = [0] * (N+1) # 정점번호는 1부터 N까지의 정수

    for i in range(1, N+1):
        tmp = input().split() # 1 - 2 3

        tree[int(tmp[0])] = tmp
    # print(tree)
    # [0, ['1', '-', '2', '3'], ['2', '-', '4', '5'], ['3', '10'], ['4', '88'], ['5', '65']]

        # 이 아래가 지워지고 def에서 int처리 해주는 것!
        # tmp 길이가 4일때, 0번 인덱스 : 정점번호, 1번 인덱스 : 연산자, 2번 인덱스 : 왼자번, 3번 인덱스: 오자번
        # if len(tmp) == 4: # 왼쪽자식과 오른쪽 자식이 둘다 있는 것
        #     tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
        #     tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        # else :
        #     tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])

    print('#{} {}'.format(tc, int(calc(1))))