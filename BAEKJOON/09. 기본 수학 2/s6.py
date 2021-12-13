def prime_list(num):
    max_num = int(num ** 0.5)
    for i in range(2, max_num + 1):
        if check[i]:           # i가 소수인 경우
            for j in range(i+i, num, i): # i이후 i의 배수들을 False 판정
                check[j] = False

    # 소수 목록 산출
    return [i for i in range(2, num) if check[i]]

for _ in range(int(input())):
    n = int(input())
    check = [True] * n
    p_list = prime_list(n)
    min_num = n // 2
    for i in range(min_num, n):
        if check[i]:
            first_even, second_even = n - i, i
            if check[first_even]:
                break
    print(first_even, second_even)

