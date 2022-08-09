def maxSubArray(nums: list[int]) -> int:
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = current_sum + nums[i] if current_sum + nums[i] >\
                                               nums[i] else nums[i]

        max_sum = current_sum if current_sum > max_sum else max_sum
    print(max_sum)


if __name__ == '__main__':
    maxSubArray([-2,1,-3,4,-1,2,1,-5,4])