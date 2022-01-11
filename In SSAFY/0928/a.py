from collections import defaultdict
input = [(30, 54), (30, 2), (30, 45), (54, 1), (45, 123), (30, 5),(2, 4), (54, 6)]
tree = defaultdict(list)
for item in input:
    tree[item[0]].append(item[1])
n = 30
print(tree)

def print_tree(v, n):
    print('[',v,']',end='',sep='')
    cnt = len(tree[v])
    if cnt == 0:
        print()
    elif cnt == 1:
        print('-----',end='')
        print(tree[v])
        return
    else:
        for i, v in enumerate(tree[v]):
            if i == 0:
                print('--+--', end='')
                print_tree(v, n+1)
            elif i == cnt-1:
                print('    '*n,'     '*(n-1), 'L--', end='',sep='')
                print_tree(v, n+1)
            else:
                print('    '*n,'     '*(n-1), '+--', end='',sep='')
                print_tree(v, n+1)

print_tree(30, 1)