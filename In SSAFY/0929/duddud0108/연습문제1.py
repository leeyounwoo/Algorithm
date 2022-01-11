'''
0000000111100000011000000111100110000110000111100111100111111001100111
'''
nums = input()
ans = []
for i in range(0, len(nums), 7):
    ans.append(int(nums[i:i+7], 2))
print(*ans, sep=',')