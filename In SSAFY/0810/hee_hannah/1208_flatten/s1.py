import sys
sys.stdin = open('input.txt')
# sol 1
for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    while dump:

        max_box = max(box)
        min_box = min(box)
        max_index = box.index(max_box)
        min_index = box.index(min_box)

        box[max_index] -= 1
        box[min_index] += 1
        dump -= 1

    print('#{} {}'.format(tc, max(box) - min(box)))
