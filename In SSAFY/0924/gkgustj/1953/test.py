a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print(max(map(max, (map(max, a)))))