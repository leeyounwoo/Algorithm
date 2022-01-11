
def binary_search(key, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        middle = (start + end) // 2

        if data[middle] == key:
            return middle # 찾았을 경우 그 때의 위치 반환

        if data[middle] > key: # 9 > 7 7은 왼쪽에잇을테니까
            end = middle - 1
        else:
            start = middle + 1

    return -1 # 검색 실패한 경우

# Q. 주어진 data 에서 11을 찾으세요
# 만약에 없으면 -1을 리턴하세요

key = 7

data = [2, 4, 7, 9, 11, 19, 23]

result = binary_search(key, data)
print(result) # 7은 2번째에 위치

key = 100

data = [2, 4, 7, 9, 11, 19, 23]

result = binary_search(key, data)
print(result) # 100은 없음