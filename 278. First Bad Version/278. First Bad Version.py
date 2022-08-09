# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def firstBadVersion(n) -> int:
    left, right = 1, n

    if isBadVersion(left):
        return left

    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

def isBadVersion(n: int) -> bool:
    if n < 4:
        return True
    else:
        return False

if __name__ == '__main__':
    firstBadVersion(5)