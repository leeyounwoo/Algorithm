def solution(s):
    new_s = ''
    for i in range(len(s)):
        word = s[i]
        if word == ' ' or word in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
            new_s += word
        else:
            if i == 0 or s[i-1] == ' ':
                new_s += word.upper()
            else:
                new_s += word.lower()
    return new_s

print(solution("3people  unFollowed me"	))