def twoSum(nums: list[int], target: int) -> list[int]:
    hashMap = {}

    for i, n in enumerate(nums):
        sec = target - n
        if sec in hashMap:
            return [hashMap[sec], i]
        hashMap[n] = i
    return


if __name__ == '__main__':
    twoSum([2,7,11,15],9)