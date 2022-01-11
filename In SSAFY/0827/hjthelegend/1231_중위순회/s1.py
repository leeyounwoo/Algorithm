import sys
sys.stdin = open('input.txt')
def inorder(n):
    if n:
        inorder(info[1][n])
        answer.append(info[0][n])
        inorder(info[2][n])


for tc in range(1, 11):
    n = int(input())

    incoming = [input().split() for _ in range(n)]
    info = [[0] * (n+1) for _ in range(3)]
    for x in incoming:
        idx = int(x[0])
        for i in range(1, len(x)):
            if i > 1:
                x[i] = int(x[i])
            info[i - 1][idx] = x[i]
    answer = []
    inorder(1)
    print('#{} {}'.format(tc, ''.join(answer)))

    # 이 문제는 다시 봐야함.. 아직 트리에 대한 이해가 부족