from typing import List


def search(nums: List[int], target: int) -> int:
    if target not in nums:
        return -1

    return nums.index(target) # Alright, alright, alright...
    
##################################################

if __name__ == '__main__':
    print(search([4,5,6,7,0,1,2], 0))
    print(search([4,5,6,7,0,1,2], 3))
    print(search([1], 0))