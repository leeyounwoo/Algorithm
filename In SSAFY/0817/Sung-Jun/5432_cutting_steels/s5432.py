import sys
sys.stdin = open('input.txt')

T= int(input())

for tc in range(1):
    iron = input()
    print(iron)
    print(len(iron))
    print(iron.count('()'))