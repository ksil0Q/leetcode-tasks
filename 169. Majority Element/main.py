from collections import Counter


def majorityElement(nums: list[int]) -> int:
    print(Counter(nums).most_common()[0][0])


majorityElement([1,1,1,1,2,2,2,2,1])
