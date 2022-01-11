import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print("#{} {}".format(tc+1, 1))
    else:
        print("#{} {}".format(tc+1, 0))

# 강사님 풀이
# for tc in range(T):
#     s1 = input()    # XYPV
#     s2 = input()    # EOGGXYPVSY
#
#     # s1의 길이만큼 슬라이딩 윈도우 생성
#     window = len(s1)
#
#     # s1의 길이만큼 하나씩 확인
#     result = 0
#     for i in range(len(s2) - window + 1):
#         if s1 == s2[i:i + window]:
#             result = 1
#             break
#     print("#{} {}".format(tc+1, result))