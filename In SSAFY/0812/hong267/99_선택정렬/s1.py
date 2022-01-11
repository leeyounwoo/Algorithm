# 선택정렬

list1 = [13, 5, 6, 0, 3, 4, 9, 0, 1, 8]

for i in range(len(list1)-1):
    min_idx = i
    for j in range(i+1, len(list1)):
        if list1[min_idx] > list1[j]:
            min_idx = j
    list1[min_idx], list1[i] = list1[i], list1[min_idx]

print(list1)