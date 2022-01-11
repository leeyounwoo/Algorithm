t = int(input())

for tc in range(1, 1+t):
    s1 = input() # XYPV
    s2 = input() # EOGGXYPVSY

    counter_dict = {}
    for char in s1:
        counter_dict[char] = s2.count(char)

    result = max(counter_dict.items(), key=lambda pair: pair[1])[1]
    print('#{} {}'.format(tc, result))

