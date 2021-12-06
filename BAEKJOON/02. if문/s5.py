hour, minute = map(int, input().split())
new_minute = minute - 45
if new_minute < 0:
    hour -= 1
    if hour < 0:
        hour += 24
    new_minute += 60

print(hour, new_minute)