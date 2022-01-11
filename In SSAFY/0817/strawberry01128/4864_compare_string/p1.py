import sys
sys.stdin = open('input.txt')
def Bigyo(first, second):
    i = 0
    j = 0
    first_length = len(first)
    second_length = len(second)
    while j < first_length and i < second_length:
        if second[i] != first[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == first_length:
        return 1
    else:
        return 0


T = int(input())
for test_case in range(1,T+1):
    first = input()
    second = input()
    firtst_length = len(first)
    second_length = len(second)
    print('#{} {}'.format(test_case,Bigyo(first, second)))
