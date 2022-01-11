import sys
sys.stdin = open('input.txt')

def compare_str(str1, str2):

    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:i+len(str1)]:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    print("#{} {}".format(tc, compare_str(str1, str2)))
