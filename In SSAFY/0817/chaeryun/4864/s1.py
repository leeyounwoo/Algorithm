import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    word1 = input()
    word2 = input()

    if word1 in word2 :
        result = 1
        
    else : 
        result = 0
    

    print('#{} {}'.format(tc, result))