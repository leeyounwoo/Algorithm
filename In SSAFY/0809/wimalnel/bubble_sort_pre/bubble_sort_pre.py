data = input() # 한줄의 문자열
data = data.split() #공백 기준으로 문자열을 자른 리스트
data = map(int, data)
data = list(data)
print(data)