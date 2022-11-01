def solution(n, s):
    value, rest = divmod(s, n)
    if value == 0:
        return [-1]
    answer = [value for _ in range(n)]
    index = n - 1
    while rest:
        answer[index] += 1
        index -= 1
        rest -= 1
    return answer

print(solution(2, 9))
print(solution(2, 1))