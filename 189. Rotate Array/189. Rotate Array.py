def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)

    if k == 0 or len(nums) == 0 or len(nums) == 1:
        return None

    for i in range(1, k + 1):
        nums.insert(0, nums[-i])

    del nums[-k:]

    return None

if __name__ == '__main__':
    rotate([1,2,3,4,5,6,7], 3)

#         k = k % len(nums)
#         if len(nums)<=1 or k==0: return
#         nums[:] = nums[-k:]+nums[:-k] в 20 раз быстрее, кек