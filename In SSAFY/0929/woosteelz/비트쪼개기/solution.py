# 0000000111100000011000000111100110000110000111100111100111111001100111


binary = input()
temp = ''
for i in range(len(binary)):

    temp += binary[i]

    if i % 7 == 6:
        if i == len(binary) - 1:
            print(int(temp, 2))
        else:
            print(int(temp, 2), end=', ')
        temp = ''
