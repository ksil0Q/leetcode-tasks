from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    if target not in nums:
        return [-1, -1]
    nums_len = len(nums)
    i = 0
    left = 0
    right = nums_len - 1
    while left != right:
        i = (left + right) // 2
        if nums[i] < target:
            left = i
        elif nums[i] > target:
            right = i
        else:
            break
    
    while nums[right] == target:
        if right < nums_len - 1:
            right += 1
    else:
        if right > 0:
            right -= 1

    while nums[left] == target:
        if left > 0:
            left -= 1
    else:
        if left < nums_len - 1:
            left += 1
        
    return [left, right]
        


######################################################

if __name__ == '__main__':
    print(searchRange([5,7,7,8,8,10], 8))
    print(searchRange([5,7,7,8,8,10], 6))
    print(searchRange([], 8))
    print(searchRange([1], 1))