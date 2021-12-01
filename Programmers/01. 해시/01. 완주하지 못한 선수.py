def solution(participant, completion):
    hash = {}
    for person in participant:
        if person in hash:
            hash[person] += 1
        else:
            hash[person] = 1
    
    for person in completion:
        hash[person] -= 1
        if hash[person] == 0:
            hash.pop(person)
    ans = list(hash.keys())
    return ans[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))