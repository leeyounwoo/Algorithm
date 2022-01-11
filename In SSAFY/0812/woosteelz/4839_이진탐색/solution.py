import sys
sys.stdin = open('input.txt')

def binarySearch(start, end, target, cnt):
    first = start
    last = end
    middle = (start + end) // 2
    if middle == target:
        return cnt
    elif middle > target:
        cnt += 1
        return binarySearch(first, middle, target, cnt)
    else:
        cnt += 1
        return binarySearch(middle, last, target, cnt)

TC = int(input())

for tc in range(1, TC + 1):
    page, target_a, target_b = map(int, input().split())
    cnta = 0
    cntb = 0
    cnta = binarySearch(1, page, target_a, cnta)
    cntb = binarySearch(1, page, target_b, cntb)
    if cnta == cntb:
        print(f"#{tc} 0")
    elif cnta < cntb:
        print(f"#{tc} A")
    elif cnta > cntb:
        print(f"#{tc} B")


