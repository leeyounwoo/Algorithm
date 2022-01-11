import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = list(input().split())
    new_words = []
    for i in range(len(words)):
        if i % 2 == 0:
            new_words[i+1] = words[i]
        else:
            new_words[i//2] = words[i]
    print(new_words)
