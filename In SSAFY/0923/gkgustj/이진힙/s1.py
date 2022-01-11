import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    tree = [0]
    for number in numbers:
        tree.append(0)
        curr = len(tree) - 1

        # 현재 삽입할 숫자가 부모보다 작다면, 부모와 계속해서 비교하며 재배치
        while curr > 1:
            if number < tree[curr//2]:
                tree[curr] = tree[curr//2]
                curr //= 2
            else:
                break

        tree[curr] = number
    
    answer = 0
    i = (len(tree) - 1) // 2

    while i > 0:
        answer += tree[i]
        i //= 2
    
    print('#{} {}'.format(t, answer))