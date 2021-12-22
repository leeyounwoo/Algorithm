import sys

sys.stdin = open('input.txt')
n, m, block_cnt = map(int, sys.stdin.readline().split())
dict_map = {}
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j] not in dict_map:
            dict_map[temp[j]] = 1
        else:
            dict_map[temp[j]] += 1
keys = sorted(list(dict_map.keys()))
min_level = keys[0]
max_level = keys[-1]

ans_level = -1
ans_time = 500 * 500 * 256
for standard in range(min_level, max_level+1):
    # print(standard)
    # print(dict_map)
    temp_block_cnt = block_cnt
    time = 0
    for i in range(len(keys)-1, -1, -1):
        if keys[i] > standard:
            temp_block_cnt += ((keys[i] - standard) * dict_map[keys[i]])
            time += (2 * (keys[i] - standard) * dict_map[keys[i]])
        elif keys[i] < standard:
            temp_block_cnt -= ((standard - keys[i]) * dict_map[keys[i]])
            if temp_block_cnt < 0:
                break
            time += (dict_map[keys[i]] * (standard - keys[i]))
    else:
        if time <= ans_time:
            ans_time = time
            ans_level = standard
print('{} {}'.format(ans_time, ans_level))
