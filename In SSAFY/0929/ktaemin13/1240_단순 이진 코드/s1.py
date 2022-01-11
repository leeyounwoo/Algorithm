import sys

sys.stdin = open("input.txt")


def passcode(word):
    # 첫 시작은 0과 1 둘 중에 하나가 나오므로, 확실하게 1이 나오는 맨 끝에서부터 탐색
    # 한 줄만 보면 되므로 한 줄 탐색 후 나머지 줄은 확인 안 해도 됨.
    for i in range(N):
        for j in range(M - 1, 0, -1):
            if info[i][j]:  # info[i][j] == 1이면,
                line = i
                idx = j
                return line, idx


def change(number):  # 암호를 십진수로 변경
    dic = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }
    return dic[number]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    info = [list(map(int, input())) for _ in range(N)]

    line = passcode(info)[0]  # 인덱스 표시
    idx = passcode(info)[1]

    password = info[line][idx - 55:idx + 1]
    result = ''  # 결괏값 초기화

    for x in range(0, len(password), 7):  # 7자리 만큼 순회해야 하므로
        temp = ''  # 초기화
        for y in range(x, x + 7):
            temp += str(password[y])
        result += change(temp)

    odd = 0  # 홀/짝 초기화
    even = 0

    for a in range(7):  # **인덱스로 들어오므로 홀/짝이 반대이므로 주의!
        if a % 2:  # 조건은 홀수이지만, 실제로는 짝수이므로 합
            even += int(result[a])
        else:  # 홀수일 경우
            odd += int(result[a])
    check = odd * 3 + even + int(result[7])  # 홀수 자리의 경우 *3을, 짝수 자리의 경우 그냥 합

    if check % 10:  # 나머지가 있다면 0을 리턴
        total = 0
    else:  # 10의 배수이면 각 자리의 합을 리턴
        total = 0
        for i in range(8):
            total += int(result[i])

    print("#{} {}".format(tc, total))
