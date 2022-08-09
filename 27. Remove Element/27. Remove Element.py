

def removeElement(nums: list[int], val: int) -> int:
    nums[:] = [num for num in nums if num != val]
    print(nums, len(nums))
    return nums

if __name__ == '__main__':
    removeElement([3, 2, 2, 3], 3)
