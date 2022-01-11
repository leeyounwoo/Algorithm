# 주어진 data에서 11을 찾으세요. 만약 없으면 -1을 리턴하세요

key = 11
data = [2, 4, 7, 9, 11, 19, 23]

def binary_search(key, data):
    start = 0
    end = len(data) -  1

    while start <= end:
        middle = (start + end) // 2

        if data[middle] == key:
            return middle

        if data[middle] > key:  #9>7
            end = middle - 1
        else:
            start = middle + 1

    return -1 # 검색 실패한 경우!

key = 11
data = [2, 4, 7, 9, 11, 19, 23]

result = binary_search(key, data)
print(result)