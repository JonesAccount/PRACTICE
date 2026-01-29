# Сделайте так, чтобы число секунд отображалось в виде
# дни:часы:минуты:секунды.

time = 100000

days = time // 86400
d = time % 86400
print(100000 % 86400)
hours = time // d
h = time % 3600

minutes = time // h
s = time % 60

print(days, hours, minutes, s, sep="|")