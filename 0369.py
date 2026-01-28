from random import *

nums = []
leugth = randint(3, 20)
def randomizer(nums):
    while len(nums) < leugth:
        result = randint(1, 10)
        nums.append(result)
    return nums

list = randomizer(nums)
print(list)