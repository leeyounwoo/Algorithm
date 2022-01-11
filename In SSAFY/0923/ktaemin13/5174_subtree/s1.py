import sys
sys.stdin = open('input.txt')


def inorder(node):
    global cnt  # cnt 값 global 변수로 선언하여 사용

    if node == 0:  # 만약 input값이 0이라면 cnt return
        return

    cnt += 1  # node가 들어오면 cnt가 1 증가

    inorder(left[node])  # 결괏값이 나오면 재귀로 cnt값 증가 ...
    inorder(right[node])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0]*(E+2)  # 왼쪽 자식노드
    right = [0]*(E+2)  # 오른쪽 자식노드

    for i in range(0,len(arr), 2):
        parent, children = arr[i], arr[i+1]
        if left[parent]:  # 왼쪽 자식노드에 값이 있다면
            right[parent] = children  # 오른쪽 자식 노드에 저장
        else:  # 왼쪽 자식노드에 값이 없다면
            left[parent] = children  # 왼쪽 자식노드에 저장

    cnt = 0
    inorder(N)
    print('#{} {}'.format(tc, cnt))
