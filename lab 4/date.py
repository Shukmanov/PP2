from datetime import datetime, timedelta

now = datetime.now()

print(now - timedelta(days=5))

# yesterday, tomorrow, today

print(now)
print(now + timedelta(days=1))
print(now - timedelta(days=1))


#drop microsec

now_without_micsec = now.replace(microsecond=0)
""" now.strftime("%m/%d/%Y, %H:%M:%S) """

print(now_without_micsec)

#difference 2 days

sec = int(input())

day1 = datetime.now()
day2 = day1 - timedelta(seconds=sec)
print(day1)
print(day2)

diff = day1 - day2
print(diff)

diff_only_seconds = diff.seconds

print(diff_only_seconds)