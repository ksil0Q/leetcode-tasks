def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    
    longest_str = ''
    length = 1

    while length <= len(s):
        i = 0
        while i + length <= len(s):
            cur_str = s[i: i + length]

            longest_str = cur_str[::-1] == cur_str and cur_str or longest_str
            i += 1

        length += 1

    return longest_str


print(longestPalindrome("babad"))