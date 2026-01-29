numc = {"coal": 145, "iron": 23, "gold": 5, not True: 55, (4,): 100, (3, "Text"): 1}

print(numc["iron"] + numc["coal"] + numc["gold"])
print(numc[not True])
print(numc[(4,)])
print(numc[(3, "Text")])