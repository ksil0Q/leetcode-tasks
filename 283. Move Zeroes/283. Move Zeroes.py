def moveZeroes(nums: list[int]) -> None:
    zeros = nums.count(0)
    while zeros > 0:
        nums.remove(0)
        nums.append(0)
        zeros -= 1
    print(nums)
    return None


if __name__ == '__main__':
    moveZeroes([0,1,0,3,12])

    #хз как ускорить, append долгий