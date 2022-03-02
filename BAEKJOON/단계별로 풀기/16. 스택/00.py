import sys


def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
