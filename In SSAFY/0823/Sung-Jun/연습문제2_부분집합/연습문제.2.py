def powerset(arr, idx, curr):
    # arr: 전체 배열
    # idx: 전체 배열에서 현재 뽑거나 뽑지 않을 위치
    # curr: 현재까지의 부분집합

    if idx == len(arr):
        #여기서 하고 싶은일
        if sum(curr) == 10:
            print(curr)
        return
    # idx 위치에 해당하는 원소를 뽑는 경우
    powerset(arr, idx+1, curr + [arr[idx]])

    #idx 위치에 해당하는 원소를 뽑지 않는 경우
    powerset(arr, idx+1, curr)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
powerset(arr, 0, [])