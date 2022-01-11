import sys
sys.stdin = open('input.txt')

def winner(start, end):
    '''
    1 : 가위
    2 : 바위
    3 : 보
    '''
    if

    center = (start+end)//2
    winner(start, center)
    winner(center+1, end)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))

    students = {}
    for i in range(N):
        students[i+1] = card[i]

    winner(1, N)