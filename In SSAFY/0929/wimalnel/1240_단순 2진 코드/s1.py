import sys
sys.stdin = open("input.txt")

T = int(input())

def search_idx(word):
    for i in range(N):
        for j in range(M-1, 0, -1):
            if info[i][j]:
                line = i
                idx = j
                return line, idx

# 이진수를 십진수 변환
def change(number):
    # 암호 규칙에 따라서 각각의 이진암호와 십진수를 딕셔너리로 정리
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
    # 해당되는 밸류값을 리턴해준다.
    return dic[number]



for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [list(map(int, input()))for _ in range(N)]

    # 함수를 이용해 찾은 인덱스를 다음과 같이 표현해 준다.
    line = search_idx(info)[0]
    idx = search_idx(info)[1]

    # 해당 인덱스를 적용시켜 56자리의 암호를 정리한다.
    password = info[line][idx-55:idx+1]
    # 암호 해독에 성공한 결과갚의 초기값 정의
    result = ''
    # 7단위로 돌면서 검사 - 7자리가 하나의 숫자이기 때문
    for i in range(0, len(password), 7):
        # 7자리 더할 것 초기화
        temp = ''
        # 7자리 내에서 하나씩 더해준다.
        for j in range(i, i+7):
            temp += str(password[j])
        # 더해준 값을 함수를 이용해서 숫자로 변환시켜준다.
        result += change(temp)

    # 홀수자리 숫자와 짝수자리 숫자 초기화
    odd = 0
    even = 0

    # 주의할 점은 인덱스로 들어오기 때문에 홀수가 반대이다.
    # 검증 코드는 포함시키지 않는다.
    for i in range(7):
        # 즉, 인덱스가 홀수일 경우는
        if i % 2:
            # 실제 비밀번호 짝수자리 수 이므로 합을 구해준다.
            even += int(result[i])
        else:
            # 홀수자리를 구해준다.
            odd += int(result[i])
    # 검증을 거쳐야한다.
    check = odd * 3 + even + int(result[7])

    # 검증이 10의 배수가 아니면 0을
    if check % 10:
        total = 0
    else:
        # 10의 배수이면 각각의 자리수 합을 더해준다.
        total = 0
        for i in range(8):
            total += int(result[i])


    print("#{} {}".format(tc, total))