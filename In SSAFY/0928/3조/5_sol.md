2번

![Image](https://media.discordapp.net/attachments/875587384383799376/892281316962349066/5-2-1.png?width=400&height=216)

4번

O(nlogn)

6번

```python
def generate_tree(input_list):
    tree = Tree()
    level = 0
    while input_list:
        element = input_list.pop
        idx = 0
        while input_list idx < len(tree[level]):
            node = tree[level][idx]
            if not node.firstchild.is_full:
                tree[level].node.firstchild.addnode(node)
            elif not node.secondchild.is_full:
                tree[level].node.secondchild.addnode(node)
            else:
                idx += 1
        level += 1
```

