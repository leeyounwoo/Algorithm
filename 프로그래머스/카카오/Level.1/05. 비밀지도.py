def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp1 = bin(arr1[i])[2:]
        temp2 = bin(arr2[i])[2:]
        temp1 = (list('0' * (n - len(temp1)) + temp1))
        temp2 = (list('0' * (n - len(temp2)) + temp2))
        temp3 = []
        for j in range(n):
            if temp1[j] == '0' and temp2[j] == '0':
                temp3.append(' ')
            else:
                temp3.append('#')

        answer.append(''.join(temp3))


    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))