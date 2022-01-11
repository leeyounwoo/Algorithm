import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n, m = map(int, input().split())
    cnt = 0
    while n < m:
        if n*2 <= m: # 2의 배수로 커지다가 m보다 작을때 일단 스탑
            n = n * 2
            cnt += 1
            if n == m:
                print(cnt)
                break
        elif n*2 > m:
            break

    # 2곱햇을때 m보다 커지게 된다면
    # -10 -1 +1하고 2를 곱하는게 더 가까워질지지
    if n-(m//2)30 < m-n20:  100 80 3 20

    # 아니면 m보다 작은 상태로 +1을 하는게 나은지 m-n 100 99= 1 100 89 =11

    # 같아지면 멈추고








    #
    # # 다른 자리수라면 *2 랑 -10 중에 뭐가 더 n과 가까워지는가
    # while m//10 > n//10: # 자리수가 다를때  12 2
    #     # (2자리수 이상일때)짝수일때만 2가능
    #     if m % 2 == 0 and m//10 - n//10 > 1:
    #         if abs(m//2-n) < abs(m-10-n):
    #             m = m//2
    #             cnt += 1
    #         else:
    #             m -= 10
    #             cnt += 1
    #     # (2자리수 이상일때)홀수일때는 -10만 가능
    #     elif m % 2 == 1 and m//10 - n//10 > 1:
    #         m -= 10
    #         cnt += 1
    #     # 한자리수 차이라면 +1 -1 *2 -10 다 고려 ex> 11 9
    #     if m//10 - n//10 == 1:
    #         if m % 2: # 홀수
    #             a = min(abs(m - n), abs(n - m), abs(m-10-n))
    #             if a == abs(m - n):
    #                 cnt
    #             elif a == abs(n - m):
    #
    #         else:
    #             a = abs(m - n), abs(n - m), abs(m // 2)
    #     if m//10 == n//10:
    #         break
    #
    # # 같은 자리수 -1 +1 //2중 어떤거?
    # if (n // 10) == (m // 10):