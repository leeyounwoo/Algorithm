import sys
sys.stdin = open('input.txt')

def calc(v):
    if len(tree[v]) == 2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R


for tc in range(1, 11):
    n = int(input()) # 정점의 개수
    tree = [0] * (n+1)

    for i in range(1, n+1):
        temp = input().split()
        tree[int(temp[0])] = temp

        if len(temp) == 4: # 양쪽 자식이 있는 경우
            # 0번은 정점번호
            # 1번은 연산자
            # 2번은 왼쪽
            # 3번은 오른쪽
            tree[int(temp[0])][2] = int(tree[int(temp[0])][2])
            tree[int(temp[0])][3] = int(tree[int(temp[0])][3])
        else:
            tree[int(temp[0])][1] = int(tree[int(temp[0])][1])

    # print(tree) # 확인용

    print('#{} {}'.format(tc, int(calc(1))))
