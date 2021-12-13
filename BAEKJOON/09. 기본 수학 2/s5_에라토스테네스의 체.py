def prime_list(num):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    check = [True] * num

    max_num = int(num ** 0.5)
    for i in range(2, max_num + 1):
        if check[i]:           # i가 소수인 경우
            for j in range(i+i, num, i): # i이후 i의 배수들을 False 판정
                check[j] = False

    # 소수 목록 산출
    return [i for i in range(2, num) if check[i]]

while True:
    n = int(input())
    if not n:
        break
    if n == 1:
        print(1)
        continue
    min_num = n + 1
    max_num = 2 * n
    ans = prime_list(max_num)
    min_index = 0
    for i in range(len(ans)):
        if ans[i] >= min_num:
            min_index = i
            break
    print(len(ans) - min_index)
# print(prime_list(int(input())))
