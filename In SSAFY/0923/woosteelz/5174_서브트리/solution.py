import sys


class node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class binary_tree:
    def __init__(self, data):
        # 노드 1번부터 E+1번까지 저장할 리스트 생성 후 0번 인덱스는 None으로 셋팅
        self.node_list = []

        for _ in range(E+2):
            self.node_list.append(node(None))

    def insert(self, parent, child):
        # 부모 노드의 왼쪽 자식이 비어있지 않다면 오른쪽에 삽입
        if self.node_list[parent].left:
            self.node_list[parent].right = self.node_list[child]
        # 그렇지 않다면 왼쪽에 삽입
        else:
            self.node_list[parent].left = self.node_list[child]

    def count_node(self, node):
        self.cnt += 1
        if node.left:
            self.count_node(node.left)
        if node.right:
            self.count_node(node.right)

    def return_num(self, num):
        self.cnt = 0
        self.count_node(self.node_list[num])
        return self.cnt


sys.stdin = open('0923/woosteelz/5174_서브트리/input.txt')


TC = int(input())
for tc in range(1, TC + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = binary_tree(E)
    for i in range(E):
        tree.insert(arr[i*2], arr[i*2+1])

    answer = tree.return_num(N)

    print(f"#{tc} {answer}")
