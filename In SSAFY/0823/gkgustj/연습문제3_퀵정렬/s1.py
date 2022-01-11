import sys
sys.stdin = open('input.txt')

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    less = []
    more = []
    equal = []
    for a in numbers:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quicksort(numbers)

    print('#{}'.format(t), end=' ')
    print(*quicksort(numbers))