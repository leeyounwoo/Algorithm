def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(len(candidate)):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def dfs(N, current_row, queens, final_result):
    if current_row == N:
        final_result.append(queens[:])
        return

    for candidate_col in range(N):
        if is_available(queens, candidate_col):
            queens.append(candidate_col)
            dfs(N, current_row + 1, queens, final_result)
            queens.pop()

N = int(input())
final_result = []
dfs(N, 0, [], final_result)
print(final_result)