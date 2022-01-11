import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num_box, num_work = map(int, input().split()) #박스 수, 몇회동안할지
    a = [0] * num_box #박스 개수만큼 리스트 만들기
    for i in range(1, num_work+1): #횟수마다
        L, R = map(int, input().split())
        for j in range(L-1, R):
            a[j] = i

    print('#{} {}'.format(tc, ' '.join(map(str, a))))
