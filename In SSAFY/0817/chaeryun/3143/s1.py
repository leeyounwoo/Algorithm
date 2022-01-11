import sys
sys.stdin = open('input.txt')

TC = int(input())

for t in range(1, TC+1):
    word1,word2 = input().split()
    result = len(word1)-(len(word2)-1)*word1.count(word2)

    print('#{} {}'.format(t, result))
