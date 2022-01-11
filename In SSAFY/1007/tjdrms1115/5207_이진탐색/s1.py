import sys
sys.stdin = open('input.txt')


def cross_binary_search(arr, n, L, R):
    prev = 0
    while True:
        m = (L + R) // 2
        if n == arr[m]:
            return True
        if L >= R:
            break
        elif n < arr[m]:
            if prev == 'l':
                break
            else:
                R = m - 1
                prev = 'l'
        else:
            if prev == 'r':
                break
            else:
                L = m + 1
                prev = 'r'
    return False


T = int(input())

answer = []
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    number_to_find = list(map(int, input().split()))
    # quicksort(numbers)
    numbers.sort()

    result = 0
    for num in number_to_find:
        if cross_binary_search(numbers, num, 0, N - 1):
            result += 1
    answer.append(result)

for tc in range(1, T + 1):
    print(f'#{tc} {answer[tc-1]}')
