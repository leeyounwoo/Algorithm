import sys

sys.stdin = open('input.txt')
for T in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    strings = [input() for _ in range(n)]
    flag = False
    for i in range(n):
        if flag:
            break
        for j in range(n - m + 1):
            # 가로 확인
            for k in range(m // 2):
                # 회문이 아닐 경우 break
                if strings[i][j + k] != strings[i][j + m - k - 1]:
                    break
            # break를 만나지 않았다는 것은 회문이라는 뜻
            else:
                ans = strings[i][j:j + m]
                flag = True
                break
            # 세로 확인
            for k in range(m // 2):
                if strings[j + k][i] != strings[j + m - k - 1][i]:
                    break
            else:
                ans = ""
                # 문자열 세로로 뽑아오기
                for h in range(j, j + m):
                    ans += strings[h][i]
                flag = True
                break

    print('#{} {}'.format(T, ans))