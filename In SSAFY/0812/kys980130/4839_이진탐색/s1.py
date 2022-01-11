import sys
sys.stdin = open("input.txt")
def binary_search(start, end, number):
    count = 0
    while start <= end:
        middle = int((start + end) / 2)
        if middle == number:
            return count
        elif middle > number:
            end = middle
            count += 1
        elif middle < number:
            start = middle
            count += 1

T = int(input())
for tc in range(1, T+1):
    end, a, b = map(int, input().split())
    start = 1
    a_score = binary_search(start, end, a)
    b_score = binary_search(start, end, b)
    if a_score < b_score:
        print('#{} A'.format(tc))
    elif a_score == b_score:
        print('#{} 0'.format(tc))
    elif a_score > b_score:
        print('#{} B'.format(tc))



