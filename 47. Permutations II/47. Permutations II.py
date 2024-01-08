from typing import List, Dict
from collections import Counter


def permuteUnique(nums: List[int]) -> List[List[int]]:
    nums_len = len(nums)
    res = []
    def make_permutations(counter: Dict[int, int], sub: List[int]) -> None:
        if len(sub) == nums_len:
            res.append(sub[:])
            return
        
        for num in counter:
            if counter[num]:
                counter[num] -= 1
                make_permutations(counter, sub + [num])
                counter[num] += 1
    
    if len(nums) == 1:
        return [nums]
    else:
        make_permutations(Counter(nums), [])

    return res


################################################

if __name__ == "__main__":
    print(permuteUnique([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permuteUnique([1,1,2])) # [[1,1,2], [1,2,1], [2,1,1]]