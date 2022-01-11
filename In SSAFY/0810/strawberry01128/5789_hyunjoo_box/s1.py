import sys

sys.stdin = open('input.txt')
T=int(input())
for test_case in range(T):
    N,Q = (map(int, input().split()))
    result = [0] * N
    for test_box in range(1,Q+1):
        L,R = map(int, input().split())
        # result[L-1]~result[R] 까지 test_box+1의 숫자를 넣어//
        for i in range(L-1,R):
            result[i] = test_box
    answer = list(map(str, result))
    answer = " ".join(answer)
    print('#{} {}'.format(test_case+1,answer))




