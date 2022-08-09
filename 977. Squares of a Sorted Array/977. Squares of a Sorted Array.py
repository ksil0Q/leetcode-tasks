def sortedSquares(nums: list[int]) -> list[int]:
    squares = [x ** 2 for x in nums]
    return sorted(squares)


if __name__ == '__main__':
    sortedSquares([-4,-1,0,3,10])