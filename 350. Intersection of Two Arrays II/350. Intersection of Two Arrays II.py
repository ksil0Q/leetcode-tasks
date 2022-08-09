def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) < len(nums2):
        intersection = makeIntersect(nums1, nums2, [])
    else:
        intersection = makeIntersect(nums2, nums1, [])


    print(intersection)


def makeIntersect(nums1: list[int], nums2: list[int], intersection) -> list[int]:
    for num in nums1:
        if num in nums2:
            intersection.append(num)
            nums2.remove(num)
    return intersection

if __name__ == '__main__':
    intersect([1, 2, 2, 1], [2, 2])

    # c = Counter(nums2)
    # inter = []
    # for i in nums1:
    #     if c[i] > 0:
    #         inter.append(i)
    #         c[i] -= 1 побыстрее будет