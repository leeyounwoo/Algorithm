from pprint import pprint

arr = [1, 2, 3, 4]
n = len(arr)

subsets = []
for i in range(1 << n):
    temp = []
    for j in range(n):
        if i & (1 << j):
            temp.append(arr[j])
    subsets.append(temp)

pprint(subsets)