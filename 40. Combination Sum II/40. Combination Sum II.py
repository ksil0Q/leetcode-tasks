from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def find_combinations(sub: List[int], index: int, sum_of_candidates: int) -> None:
        if sum_of_candidates > target:
            return

        if sum_of_candidates == target:
            res.append(sub[:])
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            sub.append(candidates[i])
            find_combinations(sub, i + 1, sum_of_candidates + candidates[i])
            sub.pop()

    if sum(candidates) < target:
        return []
    else:
        find_combinations([], 0, 0)

    return res


#############################################################33

if __name__ == "__main__":
    for i in range(2, 4):
        print(i)
    print(combinationSum2([10,1,2,7,6,1,5], 8)) # [ [1,1,6], [1,2,5], [1,7], [2,6] ]
    print(combinationSum2([1,2], 4)) # []
    print(combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27)) # []
    print(combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30))