import sys
sys.stdin = open('input.txt')

for i in range(1, 11):
    many_times = int(input())

    boxes = list(map(int, input().split()))

    for j in range(many_times):
        max_box = boxes[0]
        min_box = boxes[0]
        for oo in boxes:
            if max_box < oo:
                max_box = oo

            if min_box > oo:
                min_box = oo

        boxes[boxes.index(max_box)] -= 1
        boxes[boxes.index(min_box)] += 1

    result = max_box - min_box
    print('#{0} {1}'.format(i, result))