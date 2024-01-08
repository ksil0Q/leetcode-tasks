from typing import List


def canJump(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    
    if nums[0] == 0:
        return False
    
    for i, v in enumerate(nums):
        if v != 0:
            continue
        
        j = i - 1
        if i != len(nums) - 1:
            jumps_needed_count = 2
        else:
            jumps_needed_count = 1
            
        while nums[j] < jumps_needed_count:
            j -= 1
            jumps_needed_count += 1
            if j < 0:
                return False

    return True


print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
print(canJump([2, 0]))
print(canJump([2, 0, 0]))