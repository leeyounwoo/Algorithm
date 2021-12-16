ans_x = []
ans_y = []
for i in range(3):
    x, y = map(int, input().split())
    if x not in ans_x:
        ans_x.append(x)
    else:
        ans_x.remove(x)
    if y not in ans_y:
        ans_y.append(y)
    else:
        ans_y.remove(y)
print('{} {}'.format(ans_x[0], ans_y[0]))