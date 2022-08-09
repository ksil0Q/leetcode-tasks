def searchInsert(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    elif target >= nums[-1]:
        return len(nums)
    else:
        while not nums.__contains__(target):
            target += 1
        else:
            return nums.index(target)


"""
		if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
"""
if __name__ == '__main__':
    searchInsert([-1, 1, 3, 5, 6], 4)