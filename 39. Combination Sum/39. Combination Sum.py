from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    
    res = []

    def find_combinations(sub: List[int], index: int) -> None:
        sum_of_candidates = sum(sub)
        if sum_of_candidates == target:
            res.append(sub[:])
            return
        
        if sum_of_candidates > target:
            return
        
        for candidate in candidates:
            if max(sub, default=0) <= candidate:
                sub.append(candidate)
                find_combinations(sub, index + 1)
                sub.pop()

    find_combinations([], 0)

    return res


##############################################################3

if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))  # [[2,2,3],[7]]
    print(combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
