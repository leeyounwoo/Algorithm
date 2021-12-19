n, m = map(int, input().split())
hash_n = {}
for i in range(2, n+1):
    if n % i == 0:
        while True:
            new, rest = divmod(n, i)
            if not rest:
                n = new
                if i not in hash_n:
                    hash_n[i] = 1
                else:
                    hash_n[i] += 1
            else:
                break

hash_m = {}
for i in range(2, m+1):
    if m % i == 0:
        while True:
            new, rest = divmod(m, i)
            if not rest:
                m = new
                if i not in hash_m:
                    hash_m[i] = 1
                else:
                    hash_m[i] += 1
            else:
                break

ans_max = 1
ans_min = 1
for key, value in hash_n.items():
    if key in hash_m:
        ans_max *= (key ** min(hash_m[key], hash_n[key]))
        ans_min *= (key ** max(hash_n[key], hash_m[key]))
    else:
        ans_min *= (key ** hash_n[key])

for key, value in hash_m.items():
    if key not in hash_n:
        ans_min *= (key ** hash_m[key])

print(ans_max)
print(ans_min)
