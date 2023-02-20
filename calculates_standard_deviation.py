def std(nums):
    n = len(nums)
    avg = sum(nums) / n
    return avg,(sum(map(lambda e: (e - avg) * (e - avg), nums)) / n) ** 0.5

nums = [0.8545,0.8553,0.8950,0.8822,0.9035,0.8968,0.8999,0.9137,0.9045]
print(std(nums))