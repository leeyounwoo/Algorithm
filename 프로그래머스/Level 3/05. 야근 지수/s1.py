def solution(n, works):
    def add(key):
        if key in work_object:
            work_object[key] += 1
        else:
            work_object[key] = 1

    def add_count(key, count):
        if key in work_object:
            work_object[key] += count
        else:
            work_object[key] = count

    work_object = {}
    for num in works:
        add(num)

    sorted_keys = sorted(work_object.keys(), reverse=True)

    while n:
        first = sorted_keys[0]
        count = work_object[first]
        # 아직 마이너스할게 많이 남았을 때
        if count <= n:
            n -= count
            # 현재 없애기
            sorted_keys.pop(0)
            work_object.pop(first)
            next_key = first - 1
            # 만약 다음 숫자가 0이면
            if next_key == 0:
                return 0
            # 다음 숫자 추가하기
            add_count(next_key, count)
            if next_key not in sorted_keys:
                sorted_keys.append(next_key)
                sorted_keys.sort(reverse=True)
        # 이번이 마지막으로 없애는거임
        else:
            work_object[first] -= n
            next_key = first - 1
            add_count(next_key, n)
            if next_key not in sorted_keys:
                sorted_keys.append(next_key)
            break

    answer = 0
    for num in sorted_keys:
        answer += work_object[num] * (num ** 2)

    return answer

# print(solution(4, [4, 3, 3]))
# print(solution(1, [2,1,2]))