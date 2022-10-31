def solution(s):
    array = s.split()
    num_array = []
    for num in array:
        num_array.append(int(num))
    answer = str(min(num_array)) + str(max(num_array))
    return answer

print(solution("1 2 3 4"))