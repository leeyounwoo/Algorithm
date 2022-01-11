import sys


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class binary_tree:
    def __init__(self):
        self.root = None
        self.arr = [Node(None)]
        self.length = 0

    def insert(self, data):
        new_node = Node(data)
        self.arr.append(new_node)
        self.length += 1

        # root가 비어있으면 루트에 삽입
        if not self.root:
            self.root = new_node
        # 아니라면 완전이진트리의 조건을 만족시키며 삽입
        else:
            if self.length % 2:
                self.arr[self.length//2].left = new_node
            else:
                self.arr[self.length//2].right = new_node

        arr_len = self.length
        while arr_len > 1:
            if self.arr[arr_len].data < self.arr[arr_len//2].data:
                self.arr[arr_len], self.arr[arr_len //
                                            2] = self.arr[arr_len//2], self.arr[arr_len]
                if arr_len % 2:
                    self.arr[arr_len//2].right = self.arr[arr_len]
                    self.arr[arr_len//2].left = self.arr[arr_len-1]
                else:
                    self.arr[arr_len//2].left = self.arr[arr_len]

                self.root = self.arr[1]

            arr_len //= 2


sys.stdin = open('0923/woosteelz/5177_이진힙/input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    tree = binary_tree()
    for t in temp:
        tree.insert(t)
    length = tree.length//2
    answer = 0
    while length:
        answer += tree.arr[length].data
        length //= 2

    print(f"#{tc} {answer}")
