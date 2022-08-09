def containsDuplicate(nums: list[int]) -> bool:
    nums_set = set(nums)

    print(nums_set)
    print(len(nums_set))
    if len(nums) != len(nums_set):
        print(True)
        return True
    else:
        print(False)
        return False

if __name__ == '__main__':
    containsDuplicate([1])