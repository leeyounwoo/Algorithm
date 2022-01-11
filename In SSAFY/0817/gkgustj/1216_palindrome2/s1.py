import sys

sys.stdin = open('input.txt')

# 문자열에서 가장 긴 회문을 탐색하는 함수
def len_palindrome(str):
    max_len = 1

    for i in range(len(str)):
        # 회문의 시작 인덱스
        start = i
        # 회문의 끝 인덱스
        # (만약 str[start]가 A로 시작했다면 str[end]도 A로 끝나야함)
        end = str.find(str[i], start+1)

        while start < len(str):
            # end가 -1이면 start 뒤에 start와 똑같은 글자가 없으므로 최대회문길이는 1
            if end == -1:
                break
            else:
                if str[i:end+1] == str[i:end+1][::-1]:
                    if end-i+1 > max_len:
                        max_len = end-i+1

                start = end
                end = str.find(str[i], start + 1)

    return max_len

for _ in range(10):
    t = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(input()))

    max_len = 1

    # 가로로 탐색
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += arr[i][j]

        temp_len = len_palindrome(temp)
        if temp_len > max_len:
            max_len = temp_len

    # 세로로 탐색
    for j in range(100):
        temp = ''
        for i in range(100):
            temp += arr[i][j]

        temp_len = len_palindrome(temp)
        if temp_len > max_len:
            max_len = temp_len

    print('#{} {}'.format(t, max_len))