import sys
sys.stdin = open('input.txt')

# 패턴이 키 값이 되는 형태
key_dic = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    puzzle = [input() for _ in range(N)]

    # 1이 있는지 확인
    r = 0
    for i in range(N):
        if "1" in puzzle[i]:
            r = i
            break
    # 1이 있는 부분만 찾아서 저장
    puzzle = puzzle[r]

    c = M
    for i in range(M - 1, -1, -1):
        # 모든 암호는 1로 끝나서 뒤에서 탐색
        if puzzle[i] == "1":
            c = i
            break

    # 원하는 키패턴만 찾아서 저장
    pwd = puzzle[c-55:c+1]

    result = ''
    for i in range(0, 56, 7):
        temp = ''
        for j in range(i, i+7):
            temp += pwd[j]

        result += str(key_dic[temp])

    odd = 0
    even = 0

    for i in range(7):
        if i % 2:
            even += int(result[i])
        else:
            odd += int(result[i])

    check_pwd = odd * 3 + even + int(result[7])

    ans = 0
    if not check_pwd % 10:
        for i in range(8):
            ans += int(result[i])

    print("#{} {}".format(tc, ans))
