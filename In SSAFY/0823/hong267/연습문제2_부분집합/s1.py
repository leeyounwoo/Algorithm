def powerset(arr, idx, curr):
    if idx == len(arr):
        print(curr)
        return

    powerset(arr, idx+1, curr + [arr[idx]])

    powerset(arr, idx+1, curr)

arr = [1, 2, 3, 4]
powerset(arr, 0, [])