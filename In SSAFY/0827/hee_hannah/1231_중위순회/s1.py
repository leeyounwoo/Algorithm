import sys
sys.stdin = open('input.txt')


def in_order(node):
    if node != 0:
        in_order(left_node[node])
        print(node_word[node], end='')
        in_order(right_node[node])


for tc in range(1, 11):
    N = int(input())
    left_node = [0] * (N + 1)
    right_node = [0] * (N + 1)
    node_word = [0] * (N + 1)

    for _ in range(N):
        temp = input().split()
        if len(temp) == 2:
            start, word = temp
            node_word[int(start)] = word
        if len(temp) == 3:
            start, word, left = temp
            left_node[int(start)] = int(left)
            node_word[int(start)] = word
        if len(temp) == 4:
            start, word, left, right = temp
            left_node[int(start)] = int(left)
            right_node[int(start)] = int(right)
            node_word[int(start)] = word

    print('#{} '.format(tc), end='')
    in_order(1)
    print()