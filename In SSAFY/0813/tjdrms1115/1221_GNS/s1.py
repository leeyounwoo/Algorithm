T = int(input())

answer = []
for tc in range(1, T + 1):
    # 테스트 케이스 번호와 숫자의 갯수를 입력받습니다. 사실 둘 다 필요없습니다.
    nothing, N = input().split()

    # 그 뒤 문자로 된 숫자의 리스트를 입력받습니다.
    numbers = list(input().split())

    # 찾을 '문자로 된 숫자'의 목록을 가진 리스트입니다.
    numword = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 숫자의 개수를 셀 리스트입니다.
    realnumbers = [0] * 10
    # 입력받은 리스트를 탐색하면서 개수를 셉니다.
    for n in numbers:
        realnumbers[numword.index(n)] += 1

    # 출력할 숫자열을 저장할 변수입니다.
    new_numbers = ''
    # 정렬된 결과를 원하기 때문에 0부터 개수만큼 추가해줍니다.
    for i in range(10):
        for j in range(realnumbers[i]):
            new_numbers += numword[i] + ' '

    # 완성된 문자열을 출력합니다. 마지막 ' '은 확인 결과 있어도 정답처리되어 그냥 두었습니다.
    result = new_numbers
    answer.append(result)

for tc in range(1, T + 1):
    # print(f'#{tc} {answer[tc-1]}')
    print('#{0}'.format(tc))
    print('{0}'.format(answer[tc - 1]))