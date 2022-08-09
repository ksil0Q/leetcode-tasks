def singleNumber(nums: list[int]) -> int:
    xor = 0
    for n in nums:
        xor ^= n
    return xor





if __name__ == '__main__':
    singleNumber([2,2,3,1,4,1,3,5,4])