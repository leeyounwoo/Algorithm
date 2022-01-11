def powerset(k, result):

    # 여기서 할 일...
    print(result)
    for i in range(k, len(arr)):
        powerset(i+1, result + [arr[i]])

arr = [1,2,3]
powerset(0, [])