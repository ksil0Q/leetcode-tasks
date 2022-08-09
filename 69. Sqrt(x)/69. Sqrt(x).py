def mySqrt(x: int) -> int:
    i = 1
    while x - i * i > 0:
        i = i * 2
    i = i - 1 if x -  i * i != 0 else i
    print(i)


if __name__ == '__main__':
    mySqrt(63)

    # l, r = 0, x
    # while l <= r:
    #     m = (l + r) // 2
    #     if m * m == x:
    #         return m
    #     if m * m < x:
    #         l = m + 1
    #     else:
    #         r = m - 1
    # return r