import sys
sys.stdin = open('input.txt')

def calculator(node):
    if len(tree[node]) == 1:
        return int(tree[node][0])
    
    else:
        order = tree[node][0]
        num1 = calculator(int(tree[node][1]))
        num2 = calculator(int(tree[node][2]))

        if order == '+':
            return num1 + num2
        elif order == '-':
            return num1 - num2
        elif order == '*':
            return num1 * num2
        elif order == '/':
            return num1 / num2


for t in range(1, 11):
    N = int(input())

    # 값, 왼쪽자식 인덱스, 오른쪽자식 인덱스
    tree = [0 for _ in range(N+1)]
    for _ in range(N):
        temp = input().split()

        tree[int(temp[0])] = temp[1:]
    
    print('#{} {}'.format(t, int(calculator(1))))