def contains_duplicate(nums):
    helper = {}
    for number in nums:
        if number in helper:
            return True
        else:
            helper[number] = number
    return False 