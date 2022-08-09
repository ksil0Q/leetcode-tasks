def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    del nums1[m:]
    nums1.extend(nums2)
    nums1.sort()
    return

if __name__ == '__main__':
    merge([1,2,3,0,0,0], 3, [2,5,6], 3)