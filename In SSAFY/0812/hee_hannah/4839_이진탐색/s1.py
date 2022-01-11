import sys
sys.stdin = open('input.txt')

def binary_search(start, key, end):

    count = 0
    while start <= end:
        middle = int((start + end)/2)
        if middle == key:
            count += 1
            return count
        elif middle > key:
            end = middle
            count += 1
        elif middle < key:
            start = middle
            count += 1


T = int(input())

for tc in range(1, T+1):
    page, pa, pb = map(int, input().split())
    start = 1
    count_a = binary_search(start, pa, page)
    count_b = binary_search(start, pb, page)

    if count_a > count_b:
        print('#{} B'.format(tc))

    elif count_a == count_b:
        print('#{} 0'.format(tc))
    elif count_a < count_b:
        print('#{} A'.format(tc))
