string = "10 -3 7 hello 10 world -3 5"
l = string.split(" ")
l.sort()
print(l)
l_num = []
for i in range(6):
    l_num.append(l[i])
print(l_num)

for i in range(len(l_num)):
    l_num[i] = int(l_num[i])
print(l_num)

m = set(l_num)
print(m)

l_num.clear()
for i in m:
    l_num.append(i)

l_num.sort()
minimal = min(l_num)
maxi = max(l_num)
woord = ", ".join(str(l_num))
print(l_num)
print(f"мин число: {minimal}"); print(f"макс число: {maxi}")
nums = 0
res = 0
for i in range(len(l_num)):
    nums = l_num.pop()
    res += nums
    nums = 0
    
print(res)
print(l_num)
p = pow(res, 2)
print(f"степень: {p}")

slo = {
    "numbers": woord,
    "min": minimal,
    "max": maxi,
    "sum_sq": p
}

for k, v in slo.items():
    print(f"{k}: {v}")