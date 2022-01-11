# Q. 주어진 data에서 11을 찾으세요.
# 만약에 없으면 -1을 리턴하세요.
key1 = 7
key2 = 22
data = [2, 4, 7, 9, 11, 19, 23]

def binary_search(key, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) // 2

        if data[middle] == key:
            return middle

        elif data[middle] > key:
            end = middle - 1

        elif data[middle] < key:
            start = middle + 1

    return -1

ans = binary_search(key1, data)
print(ans)
