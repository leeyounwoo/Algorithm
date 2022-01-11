import sys
sys.stdin = open('0923/woosteelz/5176_이진탐색/input.txt')


class Tree:
    def __init__(self, N):
        self.arr = [0 for _ in range(N + 1)]
        self.N = N
        self.cnt = 1

    def numbering(self, num):
        if num <= self.N:
            self.numbering(num * 2)
            self.arr[num] = self.cnt
            self.cnt += 1
            self.numbering(num * 2 + 1)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    tree = Tree(N)
    tree.numbering(1)
    print(tree.arr)
    print(f"#{tc} {tree.arr[1]} {tree.arr[N//2]}")
