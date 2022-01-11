import sys
sys.stdin = open('input.txt')

def calc(v):
    if len(tree[v]) == 2: # ['3', '10']
        return int(tree[v][1]) # 10
    else: # ['1', '-', '2', '3']
        L = calc(int(tree[v][2])) # 2
        R = calc(int(tree[v][3])) # 3

        if tree[v][1] == '+':
            return L + R
        elif tree[v][1] == '-':
            return L - R
        elif tree[v][1] == '*':
            return L * R
        elif tree[v][1] == '/':
            return L / R

for tc in range(1, 11):
    n = int(input())
    tree = [0]*(n+1)
    for i in range(1, n+1):
        tmp = input().split()
        # print(tmp) ['1', '-', '2', '3'],['2', '-', '4', '5'],,
        tree[int(tmp[0])] = tmp
    # print(tree) [0, ['1', '-', '2', '3'], ['2', '-', '4', '5'], ['3', '10'], ['4', '88'], ['5', '65']]

    print('#{} {}'.format(tc, int(calc(1)))) # 정수처리를 위해 int

