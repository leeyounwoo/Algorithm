def pre_order(n):
    if n:
        print(n)
        pre_order(left[n])
        pre_order(right[n])

V = 13
temp = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

left = [0 for _ in range(V+1)]
right = [0 for _ in range(V+1)]

for i in range(V-1):
    parent, child = temp[i*2], temp[i*2+1]
    if not left[parent]:
        left[parent] = child
    else:
        right[parent] = child

pre_order(1)