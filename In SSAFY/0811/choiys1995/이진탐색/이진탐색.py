
def binary_search(key, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        middle = (start + end) // 2

        if data[middle] == key:
            return middle # 찾았을 경우 그 때의 위치 반환

        elif data[middle] > key:
            end = middle - 1
        else:
            start = middle + 1

    return -1 #검색 실패

#주어진 데이터에서 11을 찾으세요
#만약 없으면 -1 리턴
key = 11
data = [2, 4, 7, 9, 11, 19, 23]

result = binary_search(key, data)
print(result) # 7은 2번째에 위치