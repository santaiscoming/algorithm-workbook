from functools import reduce

def solve(nums):
    return reduce(lambda prev, curr: prev + curr, nums)