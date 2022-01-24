import sys


def input():
    return sys.stdin.readline().rstrip()

def preorder(now):
    global pattern_preorder
    pattern_preorder += now
    if graph[now]['left'] != '.':
        preorder(graph[now]['left'])
    if graph[now]['right'] != '.':
        preorder(graph[now]['right'])



def inorder(now):
    global pattern_inorder
    if graph[now]['left'] != '.':
        inorder(graph[now]['left'])
    pattern_inorder += now
    if graph[now]['right'] != '.':
        inorder(graph[now]['right'])


def postorder(now):
    global pattern_postorder
    if graph[now]['left'] != '.':
        postorder(graph[now]['left'])
    if graph[now]['right'] != '.':
        postorder(graph[now]['right'])
    pattern_postorder += now


sys.stdin = open('input.txt')
n = int(input())
# print(ord('A'))
graph = {chr(65+i): {'left': '', 'right': ''} for i in range(n)}
for i in range(n):
    node, left, right = map(str, input().split())
    graph[node]['left'] = left
    graph[node]['right'] = right
print(graph)

pattern_preorder = ''
preorder('A')
print(pattern_preorder)

pattern_inorder = ''
inorder('A')
print(pattern_inorder)

pattern_postorder = ''
postorder('A')
print(pattern_postorder)