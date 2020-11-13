import calendar
month, day, year = map(int, input().split())
ll = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
weekday = calendar.weekday(year, month, day)
print(ll[weekday])
