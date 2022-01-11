key = 11
data = [2, 4, 7, 9, 11, 19, 23]

def binary_serch(key, data, start, end):
    middle = (start + end) // 2
    if data[middle] == key:
        return middle
    if start > end:
        return False

    if data[middle] < key:
        return binary_serch(key, data, middle + 1, end)
    return binary_serch(key, data, start, middle)

binary_serch(key, data, 0, len(data)-1)
