byte = input()

divide_num = '0b'
arr = []
# for bit in byte:
#     count += 1
#     divide_num += bit
#     if count == 7:
#         arr.append(int(divide_num,2))
#         count = 0
#         divide_num = '0b'
for i in range(0,len(byte),7):
    new_num = divide_num + byte[i:i+7]
    arr.append(int(new_num,2))

print(','.join(map(str,arr)))