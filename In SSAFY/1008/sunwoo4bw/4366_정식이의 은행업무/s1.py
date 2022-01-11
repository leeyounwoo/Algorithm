import sys
sys.stdin = open('input.txt')

def change_to_dec(num, notation): # notation -> num이 n진수인지 알려주
    tmp = 0
    # 현재 num은 문자열이다.

    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val * (notation ** n)
    return tmp

# enumerate 몰랐을 때
def change_to_dec2(num, notation):
    tmp = 0
    n = len(num) -1
    for i in map(int, num):
        tmp += i * (notation **n)
        n -= 1
    return tmp

print(change_to_dec2('1010', 2))


# T = int(input())
# for tc in range(1, T +1):
#     bi = input()
#     tr = input()
#
#     binary=[]
