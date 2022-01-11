import sys
sys.stdin = open('input.txt')
# 반복문자 지운 후 남은 문자열의 길이 출력
# 남은 문자열이 없으면 0
# Last In First Out

T = int(input())
for tc in range(1, T+1):

    word = input()
    stack = []
    for i in range(len(word)) :     # 단어의 길이만큼 돌아
        if len(stack) == 0:         # 비어있으면 푸쉬
            stack.append(word[i])
        elif stack[-1] != word[i] : # 맨 마지막으로 들어온 애가 새로 들어올 애랑 같이 X
            stack.append(word[i])   # 푸쉬
        elif stack[-1] == word[i] : # 같으면
            stack.pop()             # 팝

    print('#{} {}'.format(tc, len(stack)))

    word = ABCCB
    stack = [A]