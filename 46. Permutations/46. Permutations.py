from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    nums_len = len(nums)

    res = []
    def make_permutations(sub: List[int]) -> None:
        if len(sub) == nums_len:
            res.append(sub[:])
            return
        
        for num in nums:
            if num not in sub:
                make_permutations(sub + [num])
    
    if len(nums) == 1:
        return [nums]
    else:
        make_permutations([])

    return res


################################################

if __name__ == "__main__":
    print(permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(permute([1]))