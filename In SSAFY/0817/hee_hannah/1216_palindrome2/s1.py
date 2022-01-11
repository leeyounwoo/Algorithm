import sys
sys.stdin = open('input.txt')

def is_pal(word):
    if word == word[::-1]:
        return True
    return False
