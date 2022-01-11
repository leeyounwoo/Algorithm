import sys
sys.stdin = open('input.txt')


def partition(numbers, L, R):
    if L < R:
        pivot = (L+R)//2
        while L < R:
            while L < R and numbers[L] < numbers[pivot]:
                L += 1
            while L < R and numbers[R] >= numbers[pivot]:
                R -= 1
            if L < R:
                if L == pivot:
                    pivot = R
                numbers[L], numbers[R] = numbers[R], numbers[L]
        numbers[R], numbers[pivot] = numbers[pivot], numbers[R]
        return R


def quicksort(numbers, L, R):
    if L < R:
        p = partition(numbers, L, R)
        quicksort(numbers, L, p-1)
        quicksort(numbers, p+1, R)


T = int(input())

answer = []
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quicksort(numbers, 0, N-1)

    answer.append(numbers)

for tc in range(1, T+1):
    print('#{}'.format(tc), *answer[tc-1])
