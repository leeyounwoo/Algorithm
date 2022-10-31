def solution(s):
    array = list(map(int, s.split()))
    return f'{min(array)} {max(array)}'
