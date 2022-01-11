import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    counter_dict = {}
    for char in str1:
        counter_dict[char] = str2.count(char)

    result = max(counter_dict.items(), key=lambda pair: pair[1])[1]
    print("#{} {}".format(tc, result))
