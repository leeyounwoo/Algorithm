import sys
sys.stdin = open('input.txt')

def binary_search(P, key):
    start = 1
    end = P
    count = 0
    while start <= end:
        middle = (start + end) // 2

        if middle == key:
            return count

        elif middle > key:
            end = middle
            count += 1
        else:
            start = middle
            count += 1

T = int(input())

for tc in range(T):
    P, A, B = map(int, input().split())
    count_A = binary_search(P, A)
    count_B = binary_search(P, B)

    if count_A > count_B:
        result = 'B'
    elif count_A < count_B:
        result = 'A'
    else:
        result = 0
    print("#{} {}".format(tc+1, result))
