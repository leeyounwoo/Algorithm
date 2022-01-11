T = int(input())
for tc in range(1, T+1):
    _ = input()
    string = input().split()
    number_map = {
        'ZRO': 0,
        'ONE': 0,
        'TWO': 0,
        'THR': 0,
        'FOR': 0,
        'FIV': 0,
        'SIX': 0,
        'SVN': 0,
        'EGT': 0,
        'NIN': 0
    }
    for word in string:
        number_map[word] += 1

    result = ''
    for key, value in number_map.items():
        # zro zro ..
        result += key + ' ' * value
    print('#{} {}'.format(tc, result))

# #sol2
# T = int(input())
# for tc in range(1, T+1):
#     _ = input()
#
#     number_map = {
#         'ZRO': 0,
#         'ONE': 1,
#         'TWO': 2,
#         'THR': 3,
#         'FOR': 4,
#         'FIV': 5,
#         'SIX': 6,
#         'SVN': 7,
#         'EGT': 8,
#         'NIN': 9
#     }
#     string = input().split()
#     string.sort(key=lambda num: number_map[num])
#     print('#{} {}'.format(tc, ' '.join(string)))
