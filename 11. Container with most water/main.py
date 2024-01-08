from typing import List

def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    area = 0
    result = 0
    while left <= right:
        area = min(height[left], height[right]) * (right - left)
        result = max(result, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result

print(maxArea([1,8,6,2,5,4,8,3,7]))