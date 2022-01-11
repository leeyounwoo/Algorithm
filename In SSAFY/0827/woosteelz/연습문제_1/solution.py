'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def print_tree():
    for i in range(len(tree)):
        print(i, tree[i][0], tree[i][1], tree[i][2])

def preorder(node):
    if not node:
        return
    print(node, end=' ')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if not node:
        return
    inorder(tree[node][0])
    print(node, end=' ')
    inorder(tree[node][1])

def postorder(node):
    if not node:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end=' ')

V = int(input())
E = V - 1
temp = list(map(int, input().split()))

tree = [[0 for _ in range(3)] for _ in range(V+1)]

for i in range(0, len(temp) - 1, 2):
    parent = temp[i]
    child = temp[i+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent

# print_tree()

print('----------preorder----------')
preorder(1)
print('\n----------------------------')

print('-----------inorder-----------')
inorder(1)
print('\n----------------------------')

print('----------postorder----------')
postorder(1)
print('\n----------------------------')