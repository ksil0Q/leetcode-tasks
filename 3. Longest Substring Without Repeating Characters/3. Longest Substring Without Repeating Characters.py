def lengthOfLongestSubstring(s: str) -> int:
    hashes = {}
    len_s = 0
    for i, char in enumerate(s):
        while i < len(s) and hash(s[i]) not in hashes.values():
            hashes[s[i]] = hash(s[i])
            len_s = max(len_s, len(hashes))
            i += 1
        else:
            hashes.clear()



    print(len_s)
    return 1


# maxSize = l = 0 это раз в 500 быстрее, тк O(n) 
# window = {}
# for r, char in enumerate(s):
#     l = window[char] + 1 if char in window and window[char] >= l else l
#     window[char] = r
#     maxSize = max(maxSize, r - l + 1)
# return maxSize


if __name__ == '__main__':
    lengthOfLongestSubstring("ccdsc")