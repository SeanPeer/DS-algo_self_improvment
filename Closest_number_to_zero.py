def findClosestNumber(nums) -> int:
    closest = nums[0]
    for x in nums:
        if abs(x) < abs(closest):
            closest = x

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


arr = [-4, -2, 1, 4, 8]

print(findClosestNumber(arr))
