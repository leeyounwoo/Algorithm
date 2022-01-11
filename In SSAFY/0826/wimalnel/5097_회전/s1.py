import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    res = M % N  # ex) 3 , 10  3개의 숫자로 이루어진걸 맨앞을 맨뒤로 10번하면
                        # 0이 처음, 1번째가 두번째, 2가 세번째숫자
                        # 10 % 3 = 1이므로 두번째 입력값 출력
    result = res

    print('#{} {}'.format(tc, data[result]))