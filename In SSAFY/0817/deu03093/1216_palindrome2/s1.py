import sys

def find_lenghtpal(arr, n):
    ans = 1
    # i는 왼쪽인덱스
    for i in range(n):
        # j는 오른쪽 인덱스
        for j in range(n - 1, i, -1):
            l = i
            r = j
            count = 0
            # 왼쪽 인덱스가 오른쪽 인덱스를 초과하면 반복문 빠져나옴
            while l <= r:
                # 같은 경우
                if arr[l] == arr[r]:
                    if l == r:
                        count += 1
                        break
                    count += 2
                    l += 1
                    r -= 1
                elif arr[l] == arr[r - 1] and arr[l + 1] == arr[r]:
                    r -= 1
                    count = 0
                elif arr[l] == arr[r - 1] and arr[l + 1] != arr[r]:
                    r -= 1
                    count = 0
                elif arr[l + 1] == arr[r] and arr[l] != arr[r - 1]:
                    l += 1
                    count = 0
                elif arr[l + 1] != arr[r] and arr[l] != arr[r - 1]:
                    l += 1
                    r -= 1
                    count = 0
            if count > ans:
                ans = count
    return ans


sys.stdin = open('input.txt')
for T in range(1, 11):
    tc = int(input())
    strings = [input() for _ in range(100)]
    ans = 1
    for i in range(100):
        # 가로배열에서 가장 긴 회문 찾기
        count_width = find_lenghtpal(strings[i], 100)
        if count_width > ans:
            ans = count_width
        # 세로배열에서 가장 긴 회문 찾기
        count_height = find_lenghtpal([strings[j][i] for j in range(100)], 100)
        if count_height > ans:
            ans = count_height

    print('#{} {}'.format(T, ans))