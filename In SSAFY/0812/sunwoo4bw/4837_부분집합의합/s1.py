import sys
sys.stdin = open('input.txt')

array_A = list(range(1,13)) # 1~12
n_A = len(array_A)
list = []  #[[], [1], [2], [1,2], [3], [1,3], [2,3]...]

for i in range(1<<n_A):
    sub_list=[]   #부분집합
    for j in range(n_A):
        if i & (1<<j):  #비트연산 shift연산자
            sub_list.append(array_A[j])
    list.append(sub_list)

T = int(input())
for tc in range(1, T+1) :
    N,K = map(int, input().split()) #부분집합 원소의 수 N, 부분집합의 합K
    # 원소의 합이 K인 부분집합의 개수
    cnt = 0
    for n in list:
        if len(n) == N and sum(n) == K :
            cnt+= 1

    print('#{} {}'.format(tc, cnt))