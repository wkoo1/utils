def std(nums):
    n = len(nums)
    avg = sum(nums) / n
    return avg,(sum(map(lambda e: (e - avg) * (e - avg), nums)) / n) ** 0.5

nums = [0.822,0.8184,0.8526,0.814,0.8604,0.8478,0.8404,0.859,0.8574]
print(std(nums))