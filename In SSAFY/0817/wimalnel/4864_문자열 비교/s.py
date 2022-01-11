import sys
# input.txt 파일에서 입력값 불러오는 코드
sys.stdin = open('input.txt')

for T in range(int(input())):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print("#{} {}".format(T+1, 1))
    else:
        print("#{} {}".format(T+1, 0))